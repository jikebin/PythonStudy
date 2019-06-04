'''
需求：爬取百度翻译的更多详情内容
技术说明和注意事项：
    1、详情的翻译内容，百度翻译都反扒机制，我们需要使用 headers进行伪装
    2、注意：Accept-Encoding(压缩类型)参数，如果加入则需要对详细内容进行解压，为了方便我们可以不加该 headers 字段
    2、注意：Content-Length(定义参数长度)，有时会导致参数接收不全

分析：
    1、获取访问连接：https://fanyi.baidu.com/v2transapi
    2、定义 form data
    3、定义 headers
    4、将输入添加到：Request()中
    5、urlopen()获取数据
在实践过程中发现的问题：
    1.百度翻译，在爬取详细信息的时候，每一个字段都有一个唯一的表示，如下：
      query:where ,'sign': '951029.680388',
      love                 198772.518981
      height                434416.148417
      只有当翻译内容与 sign对应时才会爬取成功，否则会报：998错误
    猜想：sign 应该是有 js 程序根据输入的英文算出来的一个数字，找到js该js调用，在本地生成应该可以完成。
'''
from urllib import request,parse

url = "https://fanyi.baidu.com/v2transapi"
info = input("请输入翻译内容：")

form_data = {
  'from': 'en',
  'to'  : 'zh',
  'query': info,
  'transtype': 'realtime',
  'simple_means_flag': '3',
  'sign': '951029.680388',
  'token': '38cd7601a77b490bc5fdd9b2abc72b2c',
}
form_data = parse.urlencode(form_data).encode('utf8')

# 定制headers格式
headers = {
  'authority': 'fanyi.baidu.com',
  'method': 'POST',
  'path': '/v2transapi',
  'scheme': 'https',
  'accept': '*/*',
  # 'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9',
  # 'content-length': '121',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': 'BAIDUID=BEA39B3DCA4E0E1C342452BD5CBA5BDA:FG=1; BIDUPSID=BEA39B3DCA4E0E1C342452BD5CBA5BDA; PSTM=1559533928; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[9Do93j_AhCs]=dNFpeKOr2ptnH01nHR1QhPEUf; delPer=0; H_PS_PSSID=; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1559632362; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1559632362; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=ade625e749ce07488b50eeebcf11477988f87f41_1559632359_js; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
  'origin': 'https://fanyi.baidu.com',
  'referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest',
}


req = request.Request(url=url,headers=headers)

response = request.urlopen(req,data=form_data)
with open('baidu.json','ab') as f:
  f.write(response.read())
