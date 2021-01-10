import scrapy
import pandas as pd
from scrapy_selenium import SeleniumRequest
import json
import codecs
import requests
import re
import cssselect
from lxml.html import etree

class QuotesSpider(scrapy.Spider):
    name = "books"
    # RF = random.random()

    def start_requests(self):
        yield scrapy.Request('http://opac.nlc.cn/F', callback=self.parse)


    def parse(self, response):
        
        data = pd.read_csv('C:/Users/30438/Desktop/data3.csv')
        isbns = data['isbn'].tolist()

        for ISBN in isbns[0:2]:
            response = requests.get('http://opac.nlc.cn/F')
            html_obj = etree.HTML(response.text)
            form_obj = html_obj.cssselect('form')[0]
            search_prefix = form_obj.attrib.get('action')

            search_page = search_prefix + '?func=find-b&find_code=ISB&request=' + ISBN + '&local_base=NLC01&filter_code_1=WLN&filter_request_1=&filter_code_2=WYR&filter_request_2=&filter_code_3=WYR&filter_request_3=&filter_code_4=WFM&filter_request_4=&filter_code_5=WSL&filter_request_5='
            yield SeleniumRequest(url=search_page, callback=self.parse_detail)

    def parse_detail(self, response):
        keys = response.selector.css('#td tbody td').re(r'<td style="background:#fff;" class="td1" id="bold" width="15%" valign="center" nowrap.*?>\s+(.*?)\s+</td>')
        values = response.selector.css('#td tbody td').re(r'<td style="background:#fff;" class="td1" align="left">\s+(.*?)\s+</td>')
        extras = response.selector.css('#td tbody td a::text').getall()
        values = list(map(lambda str:str.replace("<br>",""), values))

        index=0
        result = {}
        pre_key = ''

        for i in range(len(keys)):
            if len(keys[i])!=0 and keys[i]!=pre_key:
                pre_key = keys[i]
                if '<a' in values[i]:
                    if keys[i]=='著者':
                        result[keys[i]] = handle_author(values[i])
                    else:
                        result[keys[i]] = extras[index]
                    index+=1
                else:
                    result[keys[i]] = values[i]
            else:
                if len(values[i])!=0:
                    if isinstance(result[pre_key],list):
                        if '<a' in values[i]:
                            if pre_key=='著者':
                                result[pre_key].append(handle_author(values[i]))
                            else:
                                result[pre_key].append(extras[index])
                            index+=1
                        else:
                            result[pre_key].append(values[i])
                    else:
                        pre_val = result[pre_key]
                        result[pre_key] = []
                        result[pre_key].append(pre_val)
                        if '<a' in values[i]:
                            if pre_key=='著者':
                                result[pre_key].append(handle_author(values[i]))
                            else:
                                result[pre_key].append(extras[index])
                            index+=1
                        else:
                            result[pre_key].append(values[i])

        jl = codecs.open('books.jl','a','utf-8')
        jl.write(json.dumps(result,ensure_ascii=False))
        jl.write('\n')
        jl.close()

from selenium import webdriver
def handle_author(str):
    url = re.search(r'%22(.*?)%22', str, re.M|re.I).group(1)
    url = url.replace('&amp;','&')
    response = requests.get(url)
    response.encoding = 'utf-8'
    html_obj = etree.HTML(response.text)
    table_objs = html_obj.cssselect('table')
    if len(table_objs)==1:
        return table_objs[0].cssselect('td')[3].text.replace('\\n','').strip()
    else:
        table_obj = table_objs[1]
        anchor = table_obj.cssselect('a')[0]
        href = anchor.attrib.get('href')
        url = re.search(r'(.*?)\?', url, re.M|re.I).group(1) + '?func=accref&' + \
            re.search(r'acc_sequence=\d+', href, re.M|re.I).group(0)
        df = pd.read_html(url)[0]
        keyList = df[0].tolist()
        valList = df[1].tolist()
        author = {}
        for i in range(len(keyList)):
            if keyList[i] in author:
                if isinstance(author[keyList[i]],list):
                    author[keyList[i]].append(valList[i])
                else:
                    originalVal=author[keyList[i]]
                    author[keyList[i]]=[]
                    author[keyList[i]].append(originalVal)
                    author[keyList[i]].append(valList[i])
            else:
                author[keyList[i]] = valList[i]
        return author