import requests
from bs4 import BeautifulSoup

#热门
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

response.raise_for_status()


print(response.text)

with open('demo.json','w',encoding='utf-8')as f:
    f.write(response.text)

# soup = BeautifulSoup(response.text, 'html.parser')
#
# # 找到所有class="item"的<a>标签
# items = soup.find_all('a', class_='item')
#
# print(len(items))

