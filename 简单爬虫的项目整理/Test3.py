'''
需求：使用 urllib模块，爬取百度翻译的信息内容

分析：
    1、找到百度翻译的请求连接：Request URL: https://fanyi.baidu.com/sug
    2、查看表单的提交格式：kw:你好
    3、使用urllib发送请求，尝试访问
'''
from urllib import request,parse
import json

url = 'https://fanyi.baidu.com/sug'
value = input("请输入你要翻译的内容：")

form_data = {
  'kw' : value,
}

# 定制form表单二进制数据
form_data = parse.urlencode(form_data).encode('utf8')

response = request.urlopen(url=url,data=form_data)

# json解析数据
json_data = json.loads(response.read())
answers = json_data['data']

for item in answers:
  print(item['k'])
  print(item['v'])
  print()

'''
请输入你要翻译的内容：item
item
n. 项目; 一件商品(或物品); 一则，一条(新闻);

items
n. 项目; 一件商品(或物品); 一则，一条(新闻);  item的复数;

ITEMS
abbr. 图像科技与发展管理系统; 军种间检查测试鉴定和监督处; 综合遥测工程与管理系统(Inte

item code
网络 编号; 物品编号; 产品编号; 商品编号; 货品编码;

itemized
v. 列出清单;  itemize的过去分词和过去式;
'''
