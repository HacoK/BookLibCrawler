#1.启明星辰

# #coding=utf-8
# import json
# import requests

# with open('text.txt', 'r', encoding='UTF-8') as f:
#     ret = json.load(f)
#     file = open('data.txt', 'w', encoding='UTF-8')
#     for job in ret['data']['jobs']:
#         url = "https://app.mokahr.com/api/outer/ats-jc-apply/website/job"
#         data = json.dumps({"orgId": "venustech", "jobId": job['id'], "siteId": 3304})
#         headers = {
#             'Content-Type':'application/json',
#             'Host':'app.mokahr.com',
#             'Origin':'https://app.mokahr.com',
#             'Referer':'https://app.mokahr.com/campus_apply/venustech/3304',
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
#             'Accept': '*/*',
#         }
#         r = requests.post(url=url,data =data,headers=headers)
#         data = r.json()['data']
#         title = data['title']
#         commitment = data['commitment']
#         job_type = data['zhineng']['name']
#         locations = data['locations']
#         description = data['jobDescription'].replace('<strong>','').replace('</strong>','').replace('<p>','').replace('</p>','\n').replace('<br>','').replace('&nbsp;','')
#         education = data.get('education',None)
#         customFields = data.get('customFields',None)
#         try:
#             file.write(title+'\n')
#             file.write(commitment+'\t'+job_type+'\n')
#             for location in locations:
#                 file.write(location['address']+'\t')
#             file.write('\n')
#             file.write('职位描述'+'\n')
#             file.write(description)
#             if education:
#                 file.write('学历要求\t' + education)
#             for field in customFields:
#                 file.write('\n')
#                 file.write(field['name']+'\t'+field['value'])
#             file.write('\n')
#             file.write('\n')
#         except:
#             pass
        
#     file.close()

#2.天融信

# import scrapy

# class TestSpider(scrapy.Spider):
#     name = 'test'
#     start_urls = ['https://topsec.zhiye.com/social?r=&p=1^6&c=&d=&k=#jlt']

#     def parse(self, response):
#         for link in response.css('td a::attr(href)'):
#             url='https://topsec.zhiye.com'+link.get()
#             yield scrapy.Request(url,callback=self.parse_detail)

#     def parse_detail(self, response):
#         title = response.xpath('/html/body/div[1]/div[3]/div/div[1]/div/div/div/div[1]/span/text()').get()
#         header = response.css('body div.indexmain div.content.mtf168 div div.wide.mr10 div div div div.xiangqingcontain ul:nth-child(1) li::text').getall()
#         header = list(map(lambda x:x.strip(),header))
#         body = response.css('body div.indexmain div.content.mtf168 div div.wide.mr10 div div div div.xiangqingcontain div.xiangqingtext p::text').getall()
#         body = list(map(lambda x:x.strip(),body))
#         body = list(map(lambda x:x.replace('\xa0',''),body))
#         body = '\n'.join(body)

#         result = title
#         for i in range(len(header)):
#             if i%2==0:
#                 result+='\n'
#                 result+=header[i]
#             else:
#                 result+='\t'
#                 result+=header[i]
#         result += '\n'
#         result += body
#         result += '\n'
#         result += '\n'
#         with open('data.txt','a',encoding='UTF-8') as f:
#             f.write(result)

#3.360

# #coding=utf-8
# import json
# import requests

# with open('text.txt', 'r', encoding='UTF-8') as f:
#     ret = json.load(f)
#     file = open('data.txt', 'w', encoding='UTF-8')
#     for job in ret['data']:
#         if job['type']!='其他':
#             continue
#         url = "http://hr.360.cn/v2/index/getjobone"
#         params = {
#             "id": job['id']
#         }
#         headers = {
#             'Content-Type':'application/json',
#             'Host':'hr.360.cn',
#             'Referer':'http://hr.360.cn/hr/detail/'+str(job['id']),
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
#             'Accept': 'application/json',
#             'Cookie': 'PHPSESSID=vmk10fb3jqutpsb59svjjgghm0',
#             'X-Requested-With': 'XMLHttpRequest'
#         }
#         r = requests.get(url=url,params=params,headers=headers)
#         data = r.json()['data']
#         title = data['title']
#         area = data['area']
#         year = data['year']
#         position = data['position']
#         date = data['date']
#         description = data['description']
#         qualification = data['qualification']
#         try:
#             file.write(title+'\n')
#             file.write('工作地点: '+area+'\t')
#             file.write('工作经验: '+year+'\n')
#             file.write('职位类型: '+position+'\t')
#             file.write('发布时间: '+date+'\n')
#             file.write('职位描述'+'\n')
#             file.write(description+'\n')
#             file.write('任职要求'+'\n')
#             file.write(qualification+'\n')
#             file.write('\n')
#         except:
#             pass
        
#     file.close()

#4.奇安信

# #coding=utf-8
# import json
# import requests

# with open('text.txt', 'r', encoding='UTF-8') as f:
#     ret = json.load(f)
#     file = open('data.txt', 'w', encoding='UTF-8')
#     for job in ret['data']['details']:
#         if job['PostType']!='研发':
#             continue
#         url = "http://www.hotjob.cn/wt/qianxin/web/mode400/position/detail"
#         params = {
#             "postId": job['PostId'],
#             "recruitType": 2
#         }
#         headers = {
#             'Host':'www.hotjob.cn',
#             'Referer':'http://www.hotjob.cn/wt/qianxin/web/index',
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
#             'Accept': 'application/json, text/plain, */*',
#             'Cookie': 'SESSION=72c72c6c-c415-4e65-bcbd-05b0a4960390; SERVERID=9a14192e0fc7bcf22ca598c3f8cfec71|1611478111|161147632',
#         }
#         r = requests.get(url=url,params=params,headers=headers)
#         data = r.json()['data']
#         name = data['name']
#         workPlace = data['workPlace']
#         OrgName = data['OrgName']
#         Salary = data['Salary']
#         PostType = data['PostType']
#         RecruitNumber = data['RecruitNumber']
#         ReleaseTime = data['ReleaseTime']
#         serviceCondition = data['serviceCondition'].replace('<br>','')
#         workConcet = data['workConcet'].replace('<br>','')
#         try:
#             file.write(name+'\n')
#             file.write('工作地点: '+workPlace+'\t')
#             file.write('所属机构: '+OrgName+'\t')
#             file.write('薪资: '+Salary+'\n')
#             file.write('职位类别: '+PostType+'\t')
#             file.write('招聘人数: '+RecruitNumber+'\t')
#             file.write('发布时间: '+ReleaseTime+'\n')
#             file.write('招聘类型：社会招聘'+'\n')
#             file.write('职位描述'+'\n')
#             file.write(serviceCondition+'\n')
#             file.write('任职要求'+'\n')
#             file.write(workConcet+'\n')
#             file.write('\n')
#         except:
#             pass
        
#     file.close()

#5.深信服

# # coding=utf-8
# import json
# import requests
# 1.
# with open('text.txt', 'w', encoding='UTF-8') as f:
#         url = "https://hr.sangfor.com/api/api/Jobs"
#         data = json.dumps({"channelId":110,"page":1,"pageSize":600,"departmentId":0,"functionId":0,"kw":"","locationId":0,"workPlaceId":0})
#         headers = {
#             'Content-Type':'application/json;charset=UTF-8',
#             'Host':'hr.sangfor.com',
#             'Origin':'https://hr.sangfor.com',
#             'Referer':'https://hr.sangfor.com/Sociology',
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
#             'Accept': 'application/json, text/plain, */*',
#             'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImJmMU1KWlhvc0lhYjZ0OW1NV1VtMEEiLCJ0eXAiOiJhdCtqd3QifQ.eyJuYmYiOjE2MTE0OTU5ODYsImV4cCI6MTYxMTQ5OTU4NiwiaXNzIjoiaHR0cDovLzIwMC4yMDAuMS41Nzo4MDkwIiwiYXVkIjoiYXBpIiwiY2xpZW50X2lkIjoic2FuZ2Zvcl9jbGllbnQiLCJzY29wZSI6WyJhcGkiXX0.qaWvtwzlQxo1lWBKdhcG2E2AVibUCZbVOmS7ridIk59mrz_Ohchy970x9E6nSR8liPi0CcDqsYSP8hf2gGWHRSBo0rAn0oR6a7zF-Q6lRq8_D1BRsr5Tai4qm9e094fnOPnXFQefavJ30fElwUym_MB6ASDCBZjjmoirqq5rkBd2VgTGiesZRAxCk2MgGQzIBf-Q3pFtr1BzPmvdz1CLGTd0bRVmPLmhE6_lDIaexE0YfB8LElm6JjXZQsGA5QNkh5t1e-G-zNJ3YxK9O0LweMpFJESPEI8zIj1cnKMk1_5zfvnCh7Grpb_Qh1rvNlxyfJebjffBxNwYmPFsLCYQUw',
#             'Cookie':'ticket=eyJhbGciOiJSUzI1NiIsImtpZCI6ImJmMU1KWlhvc0lhYjZ0OW1NV1VtMEEiLCJ0eXAiOiJhdCtqd3QifQ.eyJuYmYiOjE2MTE0OTU5ODYsImV4cCI6MTYxMTQ5OTU4NiwiaXNzIjoiaHR0cDovLzIwMC4yMDAuMS41Nzo4MDkwIiwiYXVkIjoiYXBpIiwiY2xpZW50X2lkIjoic2FuZ2Zvcl9jbGllbnQiLCJzY29wZSI6WyJhcGkiXX0.qaWvtwzlQxo1lWBKdhcG2E2AVibUCZbVOmS7ridIk59mrz_Ohchy970x9E6nSR8liPi0CcDqsYSP8hf2gGWHRSBo0rAn0oR6a7zF-Q6lRq8_D1BRsr5Tai4qm9e094fnOPnXFQefavJ30fElwUym_MB6ASDCBZjjmoirqq5rkBd2VgTGiesZRAxCk2MgGQzIBf-Q3pFtr1BzPmvdz1CLGTd0bRVmPLmhE6_lDIaexE0YfB8LElm6JjXZQsGA5QNkh5t1e-G-zNJ3YxK9O0LweMpFJESPEI8zIj1cnKMk1_5zfvnCh7Grpb_Qh1rvNlxyfJebjffBxNwYmPFsLCYQUw; websiiteconfig={%22siteId%22:1%2C%22webSiteName%22:%22%E6%B7%B1%E4%BF%A1%E6%9C%8D%E6%8B%9B%E8%81%98%E5%AE%98%E7%BD%91%22%2C%22title%22:%22%E6%B7%B1%E4%BF%A1%E6%9C%8D%E6%8B%9B%E8%81%98%E5%AE%98%E7%BD%91%22%2C%22logoUrl%22:%22http://200.200.4.54:8100/hr-system/zhaopin/2020/08/10/98b48888e1544512a663e04eb5c843e8.jpg%22%2C%22domainName%22:%22https://zhaopin.sangfor.com%22%2C%22keywords%22:%22%E6%B7%B1%E4%BF%A1%E6%9C%8D%E6%8B%9B%E8%81%98%E5%AE%98%E7%BD%91%22%2C%22theme%22:%22#%22%2C%22copyright%22:%22<p>&copy%3B2000-2020%20%E6%B7%B1%E4%BF%A1%E6%9C%8D%E7%A7%91%E6%8A%80%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%20%E7%89%88%E6%9D%83%E6%89%80%E6%9C%89%20%E7%B2%A4ICP%E5%A4%8708126214%E5%8F%B7</p>%22%2C%22description%22:%22%E6%B7%B1%E4%BF%A1%E6%9C%8D%E6%8B%9B%E8%81%98%E5%AE%98%E7%BD%91%22}',
#             'X-Requested-With': 'XMLHttpRequest'
#         }
#         r = requests.post(url=url,data =data,headers=headers)
#         json.dump(r.json(),f,ensure_ascii=False)

# 2.
# with open('text.txt', 'r', encoding='UTF-8') as f:
#     data = json.load(f)['data']['listData']
#     file = open('data.txt', 'w', encoding='UTF-8')
#     for job in data:
#         if job['functionName']!='中高端岗位':
#             continue
#         title = job['title']
#         departmentName = job['departmentName']
#         commitment = job['commitment']
#         workPlaceText = job['workPlaceText']
#         description = job['description']
#         if description:
#             description = description.replace('<p>','').replace('</p>','\n').replace('<br>','').replace('&nbsp;','').replace('<strong>','')

#         result = title+'\n'
#         if departmentName:
#             result += departmentName+'/'
#         result += commitment+'\n'
#         result += '工作城市：'+workPlaceText+'\n'
#         if description:
#             result += description
#         result+='\n'

#         file.write(result)

#     file.close()

# # 猎聘
# # https://www.liepin.com/company-jobs/8905176/
# import scrapy
# import time
# from scrapy_selenium import SeleniumRequest

# class LiepinSpider(scrapy.Spider):
#     name = 'liepin'
#     headers = {
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
#         'Host': 'www.liepin.com',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         'Cookie': '__uuid=1611425987928.23; __s_bid=3315952b39c79092ac6db64f7e543dc049d0; _fecdn_=1; acw_tc=3ccdc15116117109461821646e3f0f62c80143f92040f12e40f79e56f435a6; JSESSIONID=506C910A636E91FA93BD54D7157C592F; fe_se=-1611711706304; __tlog=1611710948063.61%7C00000000%7CR000000075%7C00000000%7C00000000; __session_seq=11; __uv_seq=46',
#     }
#     index='https://www.liepin.com/company-jobs/7923384/'

#     def start_requests(self):
#         yield SeleniumRequest(url=self.index)

#     def parse(self, response):
#         time.sleep(1)
#         total_page = int(response.css('#company div.main section div div div:nth-child(2) div div a.last::attr(number)').get())
#         total_page += 2
#         for cur_page in range(1,total_page):
#             yield scrapy.Request(url=self.index+'pn'+str(cur_page)+'/',callback=self.extra_list,headers=self.headers)

#     def extra_list(self, response):
#         anchors = response.css('#company div.main section div div div:nth-child(2) ul li div.job-info a.title::attr(href)') .getall()
#         for anchor in anchors:
#             yield scrapy.Request(url=anchor,callback=self.parse_detail,headers=self.headers)

#     def parse_detail(self, response):
#         title = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div.title-info > h1::text').get()
#         salary = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div:nth-child(2) > div.clearfix > div.job-title-left > p.job-item-title::text').get().strip()[:-1]
#         location = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div:nth-child(2) > div.clearfix > div.job-title-left > p.basic-infor > span > a::text').get()
        
#         education = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div:nth-child(2) > div.clearfix > div.job-title-left > div > span:nth-child(1)::text').get()
#         experience = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div:nth-child(2) > div.clearfix > div.job-title-left > div > span:nth-child(2)::text').get()
        
#         description = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div.job-item.main-message.job-description > div.content').re(r'>(.*)<')
#         if len(description)==0:
#             description = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div.job-item.main-message.job-description > div.content::text').get()
#         else:
#             description = description[0]
#         description = description.replace('\xa0','').replace('<br>','\n')

#         yield {'岗位名称':title,'薪资水平':salary,'工作地点':location,'学历要求':education,'工作经验':experience,'工作描述':description}
        
# 猎聘 vip
# https://vip.liepin.com/7893220/joblist.shtml
# import scrapy
# import time
# from scrapy_selenium import SeleniumRequest

# class LiepinSpider(scrapy.Spider):
#     name = 'liepin'
#     headers = {
#         'Host': 'www.liepin.com',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'X-Requested-With': 'XMLHttpRequest',
#     'X-Alt-Referer': 'https://vip.liepin.com/7893220/joblist.shtml',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
#     'Referer': 'https://www.liepin.com/ajaxproxy.html',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Cookie': '__uuid=1611425987928.23; __s_bid=3315952b39c79092ac6db64f7e543dc049d0; _fecdn_=1; fe_se=-1611711706304; acw_tc=2760827816117366543086341e7472cec8b10f8545b9ef2839d0fd446394d1; __tlog=1611710948063.61%7C%7C%7C00000000%7C00000000; _mscid=00000000; _uuid=43027849FFA844220848574C6311AD80; JSESSIONID=95E94E7BC2B57E524478FEC91AF5FD07; __session_seq=112; __uv_seq=147'
#     }
#     index='https://vip.liepin.com/7893220/joblist.shtml'

#     def start_requests(self):
#         yield SeleniumRequest(url=self.index)

#     def parse(self, response):
#         time.sleep(1)
#         total_page = 50
#         for cur_page in range(0,total_page):
#             yield scrapy.Request(url='https://www.liepin.com/company/sojob.json?pageSize=15&curPage='+str(cur_page)+'&ecompIds=7893220&dq=&publishTime=&keywords=&_=1611737867208',callback=self.extra_list,headers=self.headers)

#     def extra_list(self, response):
#         anchors = map(lambda x:x['url'],response.json()['data']['list'])
#         for anchor in anchors:
#             yield scrapy.Request(url=anchor,callback=self.parse_detail,headers=self.headers)

#     def parse_detail(self, response):
#         title = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div.title-info > h1::text').get()
#         salary = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div:nth-child(2) > div.clearfix > div.job-title-left > p.job-item-title::text').get().strip()[:-1]
#         location = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div:nth-child(2) > div.clearfix > div.job-title-left > p.basic-infor > span > a::text').get()
        
#         education = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div:nth-child(2) > div.clearfix > div.job-title-left > div > span:nth-child(1)::text').get()
#         experience = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div:nth-child(2) > div.clearfix > div.job-title-left > div > span:nth-child(2)::text').get()
        
#         description = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div.job-item.main-message.job-description > div.content').re(r'>(.*)<')
#         if len(description)==0:
#             description = response.css('#job-view-enterprise > div.wrap.clearfix > div.clearfix > div.main > div.about-position > div.job-item.main-message.job-description > div.content::text').get()
#         else:
#             description = description[0]
#         description = description.replace('\xa0','').replace('<br>','\n')

#         yield {'岗位名称':title,'薪资水平':salary,'工作地点':location,'学历要求':education,'工作经验':experience,'工作描述':description}
