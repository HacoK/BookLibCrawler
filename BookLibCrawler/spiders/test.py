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