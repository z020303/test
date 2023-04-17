#  格式化输出
egg = "熟鸡蛋"
apple = "苹果"
banana = "香蕉"
vegetable = "香菜"
print("我喜欢吃" ,egg)
print("你喜欢吃",apple)
# 使用占位符拼接字符串，将变量拼接到字符串中
# 1.%s:将后边的变量（str）拼接到字符串中
# 后边%是个语法，左右空一格，语法规范
print("田海涛不喜欢吃%s" % vegetable)
print("田海涛不喜欢吃%s" % egg)
# %s:可以拼接任何数据类型，实际上拼接前会将其他数据类型先转换成str类型
name = "马成功"
age = 19
money = 3.1415926
print("姓名：%s\n年龄：%s\n零花钱：%s" % (name,age,money))
# %6.3s：
ABC = "1234567"
print("ABC变量是：%s" % ABC)
print("ABC变量是：%.3s" % ABC)
print("ABC变量是：%7.3s" % ABC)

# 2. %d: 可以拼接整数类型
print("小张的年龄是：%d"% age)
# %2d: 2表示变量占两个位置，如果变量长度不足，前面加空格
# 如果变量过长，就拼接变量本身长度
# %02d：0表示变量长度不足其前边加0
year = 2002
month = 3
day = 3
height = 186.6
print("%d-%d-%d" % (year,money,day))
print("%d-%2d-%d" % (year,money,day))
print("%d-%02d-%d" % (year,money,day))
print("%2d" % year)
# 如果拼接的是float，结果进行int（）转换，取整
print("%d"% height)

# 3.%f：可以拼接浮点数,默认保留小数6位
print("身高：%f"% height)

# %2f：.2保留小数点后两位
print("身高：%.2f" % height)
# %8.2f：8 表示拼接变量占8个位置，不足前边补空格，少了正常输出
print("身高：%8.2f" % height)
# 拼接的是整数（int）， 则转换数据类型为浮点数（float）
print("%f" % age)
# 4. %o，%x ： o是八进制，x是十六进制
num = 13
print("八进制：%o\t十六进制：%x" % (num,num))



