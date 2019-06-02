'''
爬虫基础：
大纲：urllib包、爬虫代理、有道词典
-------------------------------------------------------------------------------------------------------------------
urllib包：
    - request 模块
        - Request(url,data,head)
            - 参数：
                url:    地址
                data:   字典形式的 form表单数据，通过parse.urlencode(data字典).encode('utf-8')后的参数
                head:   设置User-Agent隐藏爬虫，字典格式
            - 返回值：req
                req,直接传递给 urlopen(req), 即可
        - urlopen(url,data=None)
            - 参数：
                url:可以传递字符串形式的地址，或者Request封装后的地址
                data:默认为None,不传递则按照get提交，否则按照post提交
            - 返回值：response
                response.read()         # 读取二进制形式的，网页信息
                response.geturl()       #返回地址
                response.info()         # 返回http信息
                response.getcode() return 200 表示正常
      - ProxyHandler({'https','192.168.100.100:端口号'})
          - 参数：
              字典形式的：{协议，'IP地址：端口号'}
          - 返回值：proxy_support
              传递给：build_opener(proxy_support)
      - build_opener(proxy)
          - 参数：
              ProxyHandler()的返回值
          - 返回值：opener
              opener.addheaders = [('User-Agent',....)]
              opener,再向下传递
      - install_opener(opener)
          - 参数：
              request.install_opener(opener)
              request.urlopen(url) #最终实现代理
          - 返回值：None

    - parse 模块
        - urlencode(dict类型).encode('utf-8')     #将字典类型表单编码
-------------------------------------------------------------------------------------------------------------------
代理步骤：
  1.参数是一个字典{'类型':'代理ip:端口号'}
  proxy_support = urllib.request.ProxyHandler({})
  2.定制、创建一个opener
  opener = urllib.request.build_opener(proxy_support)
  opener.addheaders = [('User-Agent',...)]
  3a.安装opener
  urllib.request.install_opener(opener)
  使用：urllib.request.urlopen(opener)  调用
  3b.调用 opener
  opener.open(url)
-------------------------------------------------------------------------------------------------------------------
有道词典：
from urllib import request,parse

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {
    'i': '么么哒',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15503855942713',
    'sign': 'cf312c7e1dfa31b72346927301fa8c82',
    'ts': '1550385594271',
    'bv': '6f014bd66917f921835d1d6ae8073eb1',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'true'
}
data = parse.urlencode(data).encode('utf-8')
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
req = request.Request(url,data,head)
response = request.urlopen(req)
print(response.read().decode("utf-8"))
-------------------------------------------------------------------------------------------------------------------
爬虫代理实例：
from urllib import request,parse
import random
url = 'https://www.whatismyip.com'

iplist = ['124.205.155.149	:9090','180.159.252.11:9000','124.79.167.34:9797']

proxy_support = request.ProxyHandler({'http':random.choice(iplist)})

opener = request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')]

request.install_opener(opener)

response = request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
'''
