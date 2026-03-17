# 1. 导入模块 --->调用方式：模块名.功能名 / 别名.功能名
# import random
# import random as rd

# for i in range(100):
#     print(rd.randint(1, 100))

# import 包名.模块名

# import utils.my_fun

# 包名.模块名.功能名
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()

# from utils import my_fun
# my_fun.log_separator1()
# my_fun.log_separator2()
# my_fun.log_separator3()

# 注意: 如果要通过 from utils import * 导入包下的所有模块, 需要 __init__.py 文件中添加 __all__=[]
from utils import *
my_fun.log_separator1()
# my_fun.log_separator4()

# print(my_var.PI)
# print(my_var.NAME)

# 2. 导入模块中的功能 from ... -----> 调用方式：功能名 / 别名
# from random import randint
# from random import randint as rint
# from random import *

# for i in range(100):
#     print(randint(1, 100))


# 相对路径: 从当前文件所在目录开始查找
# from utils.my_fun import log_separator1, log_separator3

# 绝对路径: 从项目的根目录下开始查找
# from 第2章 - python核心语法.utils.my_fun import log_separator1, log_separator3

# log_separator1()
# log_separator3()



"""
1.什么是模块?有什么用?
    模块:就是一个python文件(.py)，其中就包含了变量、函数、类，以及可执行的代码。
    作用:提高代码复用性，降低开发门槛
2.导入模块的常用语法?(导入模块的语句，一般写在py文件的开头)
    import 模块名 [as 别名]
    from 模块名 import 功能名 [as别名]
    from 模块名 import *
"""

