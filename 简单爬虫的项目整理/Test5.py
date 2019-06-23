'''
爬取豆瓣电影信息，Ajax请求分析

URL1：https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=20
URL2：https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=40

分析：
  1.输入你需要显示的信息页
  2.处理数据并拼接到url中
  3.访问连接获取数据
  4.打印数据
'''
from urllib import request,parse
import json
url = 'https://movie.douban.com/j/new_search_subjects?'

page = input("请输入你需要显示的页码：")
if int(page) > 0:
  num = (int(page)-1) * 20 
else:
  num = 0
data_query = {
  'sort': 'U',
  'range': '0,10',
  'tags': '',
  'start': num,
}
data_query = parse.urlencode(data_query)
url += data_query

# 定义请求头
headers = {
  'User-Agent':' Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}
# 创建请求对象
req = request.Request(url=url,headers=headers)

# 访问连接获取数据
response = request.urlopen(req)

print(json.loads(response.read()))