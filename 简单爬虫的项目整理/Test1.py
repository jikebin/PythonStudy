'''
使用 requests模块 爬取起点中文的章节内容地址。

选择的小说为：从吞噬开始
网址：https://book.qidian.com/info/1015216119

分析：
    1、获取网页内容
    2、使用正则先匹配整个章节目录
    3、解析每个章节的内容地址
    4、将内容保存到 BookInfo.txt 中
'''
import requests,re

html = requests.get("https://book.qidian.com/info/1015216119#Catalog")

# 匹配整个章节目录
dirTest = re.findall('<ul class="cf">(.*?)</ul>',html.text,re.S)

for test in dirTest:
  # 匹配每个章节的内容链接
  urls = re.findall('<a href="(.*?)"',test)
  for url in urls:
    with open('BookInfo.txt','a',encoding='utf8') as f:
      f.write(url)  # 将url地址写入到文件中
      f.write('\r') # 换行
      f.flush()

print("匹配完成...")