# 定义类 ----> 不推荐 动态的为对象添加属性，
# 因为这样会导致代码的可读性和可维护性变差, 不利于代码的规范化
# 定义类的目的是为了创建对象，也可以说是模板，模板有各种属性，动态添加属性过于麻烦
# 
# class Car:
#     pass
#
# # 创建对象
# c1 = Car()
# # 动态的为对象添加属性
# c1.color = "red"
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000
#
# print(c1)
# print(c1.brand)
# print(c1.__dict__) # 会将对象中的所有属性以字典的形式输出出来


# 定义类
# class Car:
#     # __init__ 方法是初始化的方法, 会在对象创建时自动调用, 可以在该方法中为对象设置对应的属性 ;
#     # self: 是第一个参数, 表示当前所创建出来的实例对象
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕, 对象属性已经添加完毕 .")
#
# # 创建对象
# c1 = Car("红色", "BMW", "X7", 800000)
# print(c1.__dict__)
#
# c2 = Car("白色", "奔驰", "E300", 450000)
# print(c2.__dict__)








# -------------------------------------- 定义类 实例方法 --------------------------------------------
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕, 对象属性已经添加完毕 .")
#
#     # 定义实例方法
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶中....")
#
#     def total_cost(self, discount, rate=0.1):
#         """
#         计算提车的总费用 , 包含两个部分: 车的价格 , 税费
#         :param discount: 折扣
#         :param rate: 税率
#         :return: 提车的总费用
#         """
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#
# # 测试
# c1 = Car("红色", "BMW", "X7", 800000)
#
# # 调用对象中的方法
# c1.running()
#
# total1 = c1.total_cost(0.9, 0.1)
# print("提车的总费用1为: ", total1)
#
# total2 = c1.total_cost(0.9)
# print("提车的总费用2为: ", total2)


"""
1.定义类时，类名的命名规范?
    大驼峰命名法，UserInfo、UserAccount
2.定义类时，__init__方法的作用?self参数的作用?
    __init__是初始化方式，对象创建时自动调用，主要用于设置对象的初始状态(设置对象属性)
    self是类中定义的方法的第一个参数，表示当前创建的实例对象
"""



# --------------------------------------------- 定义类 魔法方法 -----------------------------------------
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕, 对象属性已经添加完毕 .")
#
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶中....")
#
#     def total_cost(self, discount, rate=0.1):
#         total_cost = self.price * discount + rate * self.price
#         return total_cost
#
#     # 魔法方法
#     def __str__(self):
#         return f"{self.color} {self.brand} {self.name} {self.price}"
#
#     def __eq__(self, other):
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
#
#     def __lt__(self, other):
#         return self.price < other.price
#
# # 测试
# c1 = Car("白色", "BYD", "汉", 180000)
# print(c1)
#
# c2 = Car("白色", "BYD", "汉", 180001)
# print(c2)
#
# print(c1 == c2)
#
# print(c1 > c2)

"""
1.什么是魔法方法?
    Python中提供的__xxx__形式的特殊方法
    魔法方法无需手动调用，Python会在合适的时机自动调用
2.常用的魔法方法有哪些，作用是什么?
    __init__
    __str__
    __eq__
    __lt__ , __le__, __gt__ , __ge__
    <    ,   <=  ,    >   ,   >=
    little than, less than or equal to, greater than, greater than or equal to
"""


# -------------------------------- 实例属性 与 类属性 --------------------------------
class Car:
    # 类属性 (所有实例对象共享的)
    wheel = 4 # 轮胎数量
    tax_rate = 0.1 # 购置税税率

    def __init__(self, c_color, c_brand, c_name, c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中....")

    def total_cost(self, discount, rate=0.1):
        total_cost = self.price * discount + rate * self.price
        return total_cost

# 测试
c1 = Car("白色", "BYD", "汉", 180000)
print(c1.brand)
print(c1.wheel) # 通过实例对象, 查找属性时, 会先查找实例属性; 实例属性不存在, 再查找类属性

# 通过类名访问类属性
print(Car.wheel)

# c2 = Car("黑色", "Tesla", "Model Y", 260000)
# print(c2)






