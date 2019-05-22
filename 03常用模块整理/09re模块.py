'''
模块：re
大纲：应用场景、11个元字符 + 6个方法 、细节补充
应用场景：
    精确匹配用字符串，模糊匹配用正则
11个元字符：
    字符匹配相关：
        .       匹配任意一个字符
        []      匹配字符集中的一个字符
        ()      将小括号中的内容当成一个整体匹配，()内的优先级最高, (?:) 取消优先级
    匹配数量相关
        *       0到多
        +       1到多
        ？      0到1
        {}      范围匹配
    其他补充：
        ^       两种用法：[]中表示取反，[]外表示匹配开头
        $       表示结尾
        |       表示或者，在()分组时使用，例：(\d)|3  匹配左边的或者右边的，优先匹配左边的
        \       用法1：表示转义，例：\d数字   \w字符（英文+数字） \s空白字符（空白和换行）  \b单词边界（大写都表示取反）
                用法2：后面跟元字符，去除特殊功能
    特别说明：
        在[]中只有\ ^ - 带有元字符功能
6个方法：
    re.findall(pattern,string)          #匹配所有
    ret = re.search(pattern,string)     #返回对象，并且只匹配第一个  ret.group()显示匹配内容
    re.match()                          #只在字符串的开始匹配，相当于search加^(开始匹配),也需要调用group()
    re.split()                          #字符串分割
    re.sub()                            #替换
    re.compile()                        #将正则表达式封装成对象，然后通过该对象调用上面的5个方法
细节补充：
    \匹配问题：
        解决方式一：正则部分r"\\"    str='\' 说明：匹配出来的是 [\\],在str中 一个\代表两个\\。原因：python解释器转义一次，re模块转义一次
        解决方式二：正则部分 '\\\\'  str='\' 说明：匹配出来的是[\\],理由如上
    [js]分割顺序：
        先按照j分割，然后再按照s进行分割
    ()组的优先级：
        ()组的优先级默认是最高的，在匹配的过程中，会只取组内的匹配数据
        (?:) 该操作是取消组的优先级

'''
import re
str = '123456,789djd,nndnd'
#ret = re.findall("n",str)
# obj = re.search("n",str)
# ret = obj.group()
# obj = re.match("\d+",str)
# ret = obj.group()
#ret = re.split(",",str)
#ret = re.sub("\d","ni",str)
obj = re.compile("d")
ret = obj.findall("dd")
#ret = re.findall('www.(?:\w+)','www.baidu.com')
#ret = re.findall("\\\\","\d")  # [\\]
#ret = re.findall("\bsm","sm")  #[] 没有匹配到
#ret = re.findall(r"\bsm","sm")  #['sm'] 可以匹配到
#ret = re.split('[js]',"djmsll")
print(ret)
