# 变量是什么
"""
Python一切皆对象
变量：在程序运行过程中会发生变化，叫变量
命名规则：字母，数字，下划线，不能以数字开头
本质就是在程序运行过程中，在内存开辟一块空间，变量名就指向这个地方，可以代表里面数据
相同的数据会放在同一个地址中
"""
# 将右边的值 赋值给左边的变量名
# =：赋值符号    ==： 判断左右两边是否相等
name = "海绵宝宝"
print(name)
age = 20
work = "做汉堡"
car = "腿着"
print("姓名",name)
print("年龄：",age)
print ("工作：",work)
print("上班：",car)
# id():函数，查看数据的内存地址
print(id(name))
new_name = "海绵宝宝"
print(new_name,id(new_name))
zhen = True




