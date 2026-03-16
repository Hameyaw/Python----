# 采用面向对象编程思想完成如下需求
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
# 5.退出购物车
"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
    1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        1.1.录入商品名称，以及其价格、数量，保存到购物车中
        1.2.验证价格和数量范围是否合法，价格必须大于0
        1.3.创建商品对象并添加到系统
    2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        2.1.输入要修改的商品名称
        2.2.根据商品名称查找该商品对象，输出该商品的当前信息
        2.3.输入新的价格和数量，检查其是否合法
        2.4.更新购物车中的商品信息
    3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4.查询购物车:将购物车中的商品信息展示出来
        4.1格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
    5.退出购物车
"""


# 定义购物车类

class ShoppingCart:
    def __init__(self, name, price ,count):
        self.name = name
        self.price = price
        self.count = count
    # "商品名称:xxx，商品价格:xxx，商品数量:xxx"
    def __str__(self):
        return f"商品名称:{self.name}，商品价格:{self.price}，商品数量:{self.count}"
    
    # 修改购物车的商品信息
    def update_info(self, price=None, count=None):
        if price is not None:
            self.price = price
        if count is not None:
            self.count = count
           
# 购物车管理系统类

class BuyManagement:
    system_version = "1.0"
    system_name = "购物车管理系统"

    def __init__(self):
        self.cart_list = [] # 列表，记录购物车中的商品信息
    
    # 添加商品
    def add_cart(self):
        name = input("请输入商品名称:")

        # 验证商品名称是否已存在，如果商品不存在，再添加(存在则，不添加)
        for cart in self.cart_list:
            if cart.name == name:
                print("该商品已存在，无法添加")
                return
            
        self.price = float(input("请输入商品价格:"))
        self.count = int(input("请输入商品数量:"))

        # 验证价格和数量范围是否合法，价格必须大于0，数量大于等于0
        if self.price > 0 and self.count >= 0:
            cart = ShoppingCart(name, self.price, self.count)
            self.cart_list.append(cart)
        else:
            print("价格必须大于0，数量大于等于0，添加失败")

    # 修改商品信息
    def update_cart(self):
        name = input("请输入要修改的商品名称:")
        # 根据商品名称查找该商品对象，输出该商品的当前信息

        for cart in self.cart_list:
            if cart.name == name:
                print(f"当前商品信息:{cart}")
                price = float(input("请输入修改后的商品价格："))
                count = int(input("请输入修改后的商品数量："))

                # 验证修改后的价格和数量是否合法，价格必须大于0，数量大于等于0
                if cart.price > 0 and cart.count >= 0:
                    cart.update_info(price, count)
                    print("商品信息修改成功 ~")
                else:
                    print("价格必须大于0，数量大于等于0，添加失败")

        # 如果没有找到该商品，则提示用户没有找到该商品
        print("没有找到该商品，修改失败")
    
    # 删除商品
    def delete_cart(self):
        name = input("请输入要删除的商品名称：")
        for cart in self.cart_list:
            if cart.name == name:
                self.cart_list.remove(cart)
                print("商品删除成功 ~")
                return
        print("没有找到该商品，删除失败")

    # 查询指定购物车的商品信息
    def query_cart(self):
        name = input("请输入要查询的商品名称：")
        for cart in self.cart_list:
            if cart.name == name:
                print(f"查询结果：{cart}")
                return
        print("没有找到该商品，查询失败")
    
    # 查询购物车中所有商品信息

    def list_cart(self):
        for cart in self.cart_list:
            print(cart)
    
    # 运行系统
    def run(self):
        print(f"欢迎使用购物车管理系统V{BuyManagement.system_version}")
        
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("1.添加商品  2.修改商品  3.删除商品  4.查询指定商品  5.查询购物车  6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()

            choice = input("请您选择要执行的操作，输入1-6：")

            match choice:
                case "1": # 添加商品
                    self.add_cart()
                case "2": # 修改商品
                    self.update_cart()
                case "3": # 删除商品
                    self.delete_cart()
                case "4": # 查询指定商品
                    self.query_cart()
                case "5": # 查询购物车
                    self.list_cart()
                case "6": # 推出系统
                    print("感谢使用购物车管理系统，欢迎下次再来！")
                    return
                case _: # 其他输入
                    print("输入有误，请输入1-6之间的数字！")


# 下面是测试代码
if __name__ == "__main__":
    buy_management = BuyManagement()
    buy_management.run()


        




