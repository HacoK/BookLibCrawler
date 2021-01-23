#coding=utf-8
import json
import requests

with open('text.txt', 'r', encoding='UTF-8') as f:
    ret = json.load(f)
    file = open('data.txt', 'w', encoding='UTF-8')
    for job in ret['data']['jobs']:
        url = "https://app.mokahr.com/api/outer/ats-jc-apply/website/job"
        data = json.dumps({"orgId": "venustech", "jobId": job['id'], "siteId": 3304})
        headers = {
            'Content-Type':'application/json',
            'Host':'app.mokahr.com',
            'Origin':'https://app.mokahr.com',
            'Referer':'https://app.mokahr.com/campus_apply/venustech/3304',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': '*/*',
        }
        r = requests.post(url=url,data =data,headers=headers)
        data = r.json()['data']
        title = data['title']
        commitment = data['commitment']
        job_type = data['zhineng']['name']
        locations = data['locations']
        description = data['jobDescription'].replace('<strong>','').replace('</strong>','').replace('<p>','').replace('</p>','\n').replace('<br>','').replace('&nbsp;','')
        education = data.get('education',None)
        customFields = data.get('customFields',None)
        try:
            file.write(title+'\n')
            file.write(commitment+'\t'+job_type+'\n')
            for location in locations:
                file.write(location['address']+'\t')
            file.write('\n')
            file.write('职位描述'+'\n')
            file.write(description)
            if education:
                file.write('学历要求\t' + education)
            for field in customFields:
                file.write('\n')
                file.write(field['name']+'\t'+field['value'])
            file.write('\n')
            file.write('\n')
        except:
            pass
        
    file.close()