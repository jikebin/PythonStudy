'''
os模块：
大纲：路径操作、文件和文件夹操作、shell方法
路径操作：
    os.getcwd()       # 展示当前工作目录(相对目录的绝对路径)
    os.sep            # 显示系统路径分隔符
    os.path.abspath() # 显示当前文件的绝对路径
    os.path.split()   # 拆分目录 和 文件名
    os.path.dirname() # 获取绝对路劲的文件夹路径
    os.path.basename()# 获取绝对路径中的文件名称
    os.path.join()    # 拼接路径（从左到右顺序拼接）
    __file__          # 显示当前文件的相对路径，pycharm会将其封装成绝对路径
文件和文件夹操作：
    os.makedirs()           # 创建多级文件夹
    os.removedirs()         # 删除多级空文件夹(文件夹不为空，则无法删除)
    os.mkdir()              # 创建单个文件夹
    os.rmdir()              # 删除单个文件夹
    os.listdir()            # 展示文件目录，以元组形式返回
    os.remove()             # 删除文件
    os.rename()             # 重命名文件/文件夹
    os.stat()               # 获取文件信息，以元组形式返回
    os.chdir()              # 更改当前工作目录路径(默认相对路径的根目录)
系统命令：
    os.system(shell命令)
#-------------------------------------------------------------------------------------------
'''
import os
#路径操作测试：
print(os.getcwd())
print(os.sep)
print(os.path.abspath("demo.py"))
print(os.path.split("C:\\Users\\yutong\\PycharmProjects\\untitled\\模块整理\\demo.py"))
print(os.path.dirname("C:\\Users\\yutong\\PycharmProjects\\untitled\\模块整理\\demo.py"))
print(__file__)
print(os.path.join("test.txt",*["user","name","path"]))
