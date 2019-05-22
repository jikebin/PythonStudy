'''
大纲：模块种类、导入级别、三种导入方式、代码测试、找到根项目的绝对路径、PyPI
模块种类：
    1.标准库模块
    2.第三方模块(PyPI)
    3.自定义模块
导入级别：
    包 > 模块 >函数/变量
    补充说明：包就是文件夹，而模块就是文件。
导入三种方式：
    方式1：
        import re,hashlib, ...
        re.findall()
    方式2：
        from re import findall,... *   as 别名
        findall()
    方式3：
        from 包名  import 模块名
代码测试：
    if __name__ == '__main__'
        # if 内部是测试代码
    说明：__name__ == '__main__' 保证，测试代码只在该文件内部执行，而其它导入该模块的文件不会执行该测试代码
根项目的绝对路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR) 

PyPI
    PyPI(Python Package Index)是python官方的第三方库的仓库
    所有人都可以下载第三方库或上传自己开发的库到PyPI。
    PyPI推荐使用pip包管理器来下载第三方库。
    这里有pypi官方社区详细介绍，大家可以进去看看   https://pypi.org/，写得很详细！
'''
import os,sys
print(__name__ == '__main__')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR) 
print(os.path.abspath(__file__))
print(BASE_DIR)
