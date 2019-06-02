'''
requests 模块的基本使用

requests 模块优点
  1.完美替代Python 的 urllib2
  2.更多的自动化
  3.更友好的用户体验
  4.更完善的功能

1.由于 requests 模块是第三方模块，所以我们需要先进行下载
2.命名如下：
      pip install requests
'''
import requests

html = requests.get('http://www.baidu.com')
print(html.text) 