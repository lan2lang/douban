from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 找到所有class="item"的<a>标签
items = soup.find_all('a', class_='item')

for item in items:
    # 输出<a>标签的链接
    print(item['href'])

    # 找到<a>标签内的<img>标签
    img_tag = item.find('img')
    if img_tag:
        print(img_tag['src'])

    # 找到<a>标签后面的<p>标签
    p_tag = item.find_next('p')
    if p_tag:
        print(p_tag.text)
