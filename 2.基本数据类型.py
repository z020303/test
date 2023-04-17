"""
在Python中一切皆对象，面向对象编程语言
人生苦短我用Python
python基本数据类型
1.数值类型：
  整型（int）：就是整数（-1,0,1）十进制（1-9）八进制（0-7） 十六进制（0-f）
  浮点型（float）：就是小数（2.0,3.14,3.1）
2.字符型：
   字符串（str）：相当于一句话，例如："拜登"，‘特朗普’，"懂王"
   注意：带引号的数字是字符串
3.布尔类型
用于条件判断的结果
TRUE ：真
FALSE：假
注意首字母大写
4.复数型
"""
print(-789)     # int
print(5.12)     # float
print("JQK")    # str
print("5.21")   # 字符串
# type():查看数据类型函数
print(type("12345"))    # class str
print(type(123))     # int
print(type(2.333))   # float
# 注意：字符串除了单双引号用法，还可以用三引号
"""
多行注释，也是字符串，写长字符串，中间可以换行
"""

print("""
   静夜思
床前明月光，疑是地上霜
举头望明月，低头思故乡
""")


# 布尔类型
# print(True)
# print(False)
# print(True == 1)
# print(8>7)
# print(9<2)
# ==

a = 2+2j
print(type(a))
print(a.real)
print(a.imag)



a = "小李子"
b = 2.36
c = 2
d = 3-3j
print(type(a),type(b),type(c),type(d))