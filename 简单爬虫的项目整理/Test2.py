'''
需求：使用urllib模块，爬取百度搜索内容

网址：https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=93153557_hao_pg&wd=%E7%A5%9E%E9%A9%AC

分析：
  1、通过键盘输入搜索信息: input()
  2、将录入信息拼接成完整的：url地址
  3、通过 urlopen()访问百度内容
  4、将内容写入到文件中
'''
from urllib import request,parse
 
start_url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=93153557_hao_pg&wd='

value = input("请输入搜索结果：")
# 将输入结果编码
end_url = parse.quote(value)
# 拼接完整的url
url = start_url + end_url

# 访问数据
response = request.urlopen(url)

# 将数据写入到文件中

# with open('file.html','wb') as f:
#   f.write(response.read())
print(response.read())
