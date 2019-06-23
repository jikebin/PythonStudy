'''
xpath原理：
    将html文档变成一个对象，然后调用对象的方法去查找指定的节点
两种使用方式：
    (1)本地文件
    tree = etree.parse(文件名)

    (2)网络文件
    tree = etree.HTML(网页内容字符串)
路径查找方法：
    ret = tree.xpath('//div[@class="..."]')    
'''
from lxml import etree

tree = etree.parse('xpathTest.html')

# 方式一：
ret = tree.xpath('//div[@class="song"]//text()')	
print(ret)  
# 结果：['\n\t火药\n\t', '造纸术', '\n\t', '印刷术', '\n\t指南针\n']

# 方式二：
ret = tree.xpath('//div[@class="song"]')
string = ret[0].xpath('string(.)')
print(string.replace('\n','').replace('\n',''))
# 结果： 火药    造纸术  印刷术  指南针