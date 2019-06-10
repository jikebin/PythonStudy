'''
大纲：
分组、贪婪模式、正则修饰符、字符串前加r的作用

分组：
    (匹配内容)      ()会将内部作为一个整体来进行匹配
    (?:匹配内容)    取消()的优先级
    \1             表示复用第一个分组，\<number> number是几就表示复用第几个分组

贪婪模式：
贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配。
非贪婪模式：非贪婪模式在整个表达式匹配成功的前提下，尽可能少的匹配。
属于贪婪模式的量词：
  {m,n}     匹配 m~n 个
  {m,}      匹配不少于 m个
  *        匹配 0到多个
  +        匹配 1到多个
取消贪婪模式：在量词后面加上?即可，如：{m,n}?   *?    +?

正则修饰符：
    re.I		忽略大小写
    re.M		多行匹配(一般用于^开头匹配，这样就可以将每一行进行单独的开头匹配)
    re.S		单行匹配(可以理解成 . 可以匹配换行符)

字符串前加r的作用：
    r加在字符串的前面，如：r'\t' 是为了防止 \ 的转义
    如：在匹配路径过程中，如：r'C:\music\time'


在线正则表达式测试工具：
  http://tool.oschina.net/regex/
  http://tool.chinaz.com/regex/
  https://c.runoob.com/front-end/854
'''
import re
# 分组演示
string = 'AAitAAitAA'
ret = re.search(r'(AA)(it)\1\2\1',string)
print(ret.group())  # 结果：AAitAAitAA

# 贪婪模式演示
str1 = '<aaabbb>cccddd>'

ret1 = re.search('<(.*)>',str1)
print(ret1.group())
# 贪婪模式结果：<aaabbb>cccddd>
ret2 = re.search('<(.*?)>',str1)
print(ret2.group())
# 非贪婪模式结果：<aaabbb>

# 正则修饰符

str2 = 'AaAaAa'

ret1 = re.search('a+',str2,re.I) 
print(ret1.group())
# 忽略大小写结果：AaAaAa
