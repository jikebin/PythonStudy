'''
模块：sys
大纲：模块说明、显示模块导入路径、显示操作系统名称
模块说明：
    1.sys模块是与python解释器交互的模块
模块导入路径：
    sys.path    #显示模块导入路径
    sys.path.append() #添加模块导入路径
显示操作系统：
    sys.platform
'''
import sys
print(sys.path)
print(sys.platform)