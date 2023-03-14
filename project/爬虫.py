import requests
from bs4 import BeautifulSoup

# 用户输入一个网址
url = input("Please enter a website URL: ")

# 连接到该网址并下载网页内容
response = requests.get(url)
html = response.content

# 解析网页内容，提取所需信息
soup = BeautifulSoup(html, 'html.parser')
# 以下为示例提取信息
# 获取网页标题
title = soup.title.string
# 获取所有链接
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

# 将提取的信息存储到文件中
with open('output.txt', 'w') as f:
    f.write(f"Title: {title}\n")
    f.write("Links:\n")
    for link in links:
        f.write(f"{link}\n")
