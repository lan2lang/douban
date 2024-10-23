import json
#热门
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'

#解析json

with open('demo.json','r',encoding='utf-8') as f:

    data=json.loads(f.read())['subjects']

print(len(data))

print(data[0]['title']+data[0]['rate'])
print(data[0]['cover'])
print(data[0]['url'])
