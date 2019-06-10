'''
大纲：
安装模块、使用方式、两种转换方式、常用的六种方式

安装模块：
  pip install bs4
  pip install lxml

使用方式：
  可以将一个 html文档，转化为指定的对象，然后通过对象的方法和属性，去查找指定内容。

两种转换方式：
  from bs4 import BeautifulSoup  
  (1)转化本地文件：
    soup = BeautifulSoup(open('本地文件'),'lxml')
  (2)转化网络文件：
    soup = BeautifulSoup('字符串类型或字节类型','lxml')

常用的6中方式：
  （1）根据标签名查找   # 例：soup.a
  （2）获取属性        # 例：soup.a['href']
  （3）获取内容        # 例：soup.a.text
  （4）find           # 查找第一个符合要求的元素
  （5）find_all       # 查找所有符合要求的元素
  （6）select         # 根据选择器，选择指定的内容

'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs4Test.html'),'lxml')

#（1）根据标签名查找：soup.标签名
print(soup.a) # 获取第一个a标签
              # 结果：<a href="www.baidu.com">百度你好</a>

#（2）获取属性：soup.标签名['属性名']
print(soup.a['href']) # 获取第一个a标签的属性名
                      # 结果：www.baidu.com

#（3）获取内容：
print(soup.a.text)		  # 获取a标签的 text 内容(可以获取标签内容部分的所有嵌套内容)
print(soup.a.get_text())# 获取a标签的 text 内容,和上面一样
# 结果：百度你好

#（4）find 
print(soup.find('a'))	                  # 找到第一个符合要求的a
# 结果：<a href="www.baidu.com" title="search">百度你好</a>
print(soup.find('a',title = 'search'))  # 通过标签属性查找指定标签
# 结果：<a href="www.baidu.com" title="search">百度你好</a>
print(soup.find('a',class_ = 'china'))  # 注意：如果是class要加 _ 因为class在python中是关键字
# 结果：<a class="china" href="www.chinaos.com">中国搜索</a>

# 多级查找
div = soup.find('div')
print(div.find('a',class_ = 'china').get_text())
# 结果：中国搜索

#（5）find_all
# 说明：find_all的用法和 find的用法相同，并支持以下两种特殊用法：

print(soup.find_all(['a','p'])) # 查找列表中所有符合要求的标签
print(soup.find_all('a',limit=2)) # 查找前两个内容
# 说明：所有内容都存储在列表中

#（6）select
# 该方法是以 css 选择器的形式来获取指定标签

print(soup.select('.china'))
# 结果：[<a class="china" href="www.chinaos.com">中国搜索</a>],注意：结果是一个列表
