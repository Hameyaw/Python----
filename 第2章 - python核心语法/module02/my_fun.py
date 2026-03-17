# __all__ 指定 from ... import * 导入的是哪些功能
__all__ = ["log_separator1", "log_separator3", "PI"]

# 常量(不会发生变化的数据 ; 常量的名称为全部大写)
PI = 3.1415926
NAME = "黑马☆涛哥"

# 函数
def log_separator1():
    print("- " * 30) # "- "重复输出30次

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

# 测试函数
# __name__ : Python中内置变量, 表示的当前模块的名字 (直接运行当前模块, __name__的值为 "__main__" ; 当该模块被导入时, __name__的值就是模块名称)
# 执行当前文件, 则会执行如下代码; 如果被当做模块导入, 如下代码不执行;
if __name__ == '__main__':
    log_separator1()

"""
1.__name__与 __all__这两个特殊变量的作用是什么?
    __name__是Python中非常重要的内置变量，表示的是当前模块的名称
    当模块直接运行时:__name__的值为"__main__"(if__name__=" __main__")
    当模块被导入时:__name__等于模块的文件名(不含.py后缀)
"""


