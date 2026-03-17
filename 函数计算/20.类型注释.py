
#变量定义-未指定类型注解--->类型推断
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None
names =["A", "C","E",100]
phones ={"13309091111","15209101902","18809019201"}
options = {"count":2 , "total":10}
goods=("手机", 6999, 1)

names.append("x")
names.append(10010)
names.append(10010.0)


#变量定义-指定类型注解
a2:int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None
names2: list[str | int] =["A", "C", "E",100]
phones2: set[str] ={"13309091111","15209101902","18809019201"}
options2: dict[str, int] = {"count":2 , "total":10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)
              
names2.append("x")
names2.append(10010)
# names2.append(10010.0)


"""_summary_
1.类型注解的写法?
    变量:数据类型(如a:int)
2.常见类型的写法
    int、float、bool、str、None、Iist、set、tuple、dict
    str | int
3.为什么要使用类型注解，有什么好处呢?
    代码结构更清晰、代码逻辑更安全、易维护
    更准确的代码自动提示
    提前发现代码潜在问题
    
如果对变量直接赋值、变量运算等场景，Python会自动进行类型推断
Python是动态类型语言，添加的类型注解只是提示，并不是强制约束!!!

"""