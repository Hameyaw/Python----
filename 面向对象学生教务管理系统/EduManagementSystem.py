
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过
# 控制台菜单与用户交互，具体的功能如下:
# 1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
# 2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
# 3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
# 4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
# 5.展示全部学生成绩:展示出系统中所有学生的成绩

"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下:
    1.添加学生成绩:根据输入的生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
        1.1输入学生姓名、语文成绩、数学成绩、英语成绩
        1.2检查学生姓名是否已存在，如果学生不存在，再添加(存在则，不添加)
        1.3验证成绩范围(0-100分)
        1.4创建学生对象并添加到系统
    2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
        2.1输入要修改的学生姓名
        2.2根据姓名查找该学生，显示该生当前成绩信息
        2.3输入新的语文、数学、英语成绩
        2.4更新学生成绩数据
    3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
    4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
        4.1输出格式为:“姓名:张三|语文:85/数学:90 |英语:88|总分:263'
    5.展示全部学生成绩:展示出系统中所有学生的成绩
"""

# 定义学生类
class Student:
    def __init__(self, name, chinese, math, english) :
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    
    # 姓名:张三|语文:85/数学:90 |英语:88|总分:263
    def __str__(self) -> str:
        return f"姓名：{self.name}|语文:{self.chinese}/数学:{self.math} |英语:{self.english}|总分:{self.chinese + self.math + self.english}"
    
    # 修改学生的成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english




# 测试
if __name__ == "__main__":
    