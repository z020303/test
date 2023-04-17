# 基本数据类型： int(整型)，float（浮点型），str（字符串），bool（布尔）
name = "泽拉斯基"
print(name,type(name))
# 1).int():函数，将其他数据转换成int整型
# 即使是纯数字的字符串也无法进行数学运算
# 将字符串转化为整型
number = "1010"
print(number)
print(1010)
# int ()函数
num = int(number)
print(num,type(num))
# int()转化字符串为整型，数据一定是纯数字，可以带符号+ -
# phone_num = "微信19337176751"
# ValueError: invalid literal for int() with base 10: '微信19337176751'
# value: 值， error: 错误
# pum = int(phone_num)
# print(pum)
# 2)将浮点型转化为整数，int()转化的时候会取小数的整数部分
z = 1.314
int1 = int(z)
print(int1,type(int1))

z2 = 0.999999
int2 = int(z2)
print(int2,type(int2))

z3 = 0.99999999999999999999999
int3 = int(z3)
print(int3,type(int3))

# 2.float():函数，将其他数据转化为float浮点型
# 1）纯数字字符串转化为浮点型
number = "1010"
float1 = float(number)
print(float1, type(float1))

# 2)整型转化为浮点型
y = 900000
float2 = float(y)
print(float2, type(float2))

# 3.str():函数，将其他数据转化为字符串
int3 = 1218
float3 = 3333
s1 = str(int3)
s2 = str(float3)
print(s1, s2, type(s1))

# 4.bool():函数，可以将其他数据类型转化布尔值
# 空格占一个位置，也是字符，""空字符串
# 当字符串转化为布尔值，长度大于0为True,长度为0是False
gg = " "
b1 = bool(gg)
print(b1,type(b1))

# len():计算字符串的长度
print(len(gg))

# 将int转化为布尔值,0 转换后False，非0是True
i1 =1
b2 = bool(i1)
print(b2)

# 3.将float转化为布尔值， 0.0可以转化为False，其他浮点数是Ture
f1 = 2.3333333         # 带小数点是浮点数
b3 = bool(f1)
print(b3)

# 4.将布尔值转化为int，float，str
int11 = 90
float11 = 3333.333
str11 = "abc"
print(bool(int11), bool(float11), bool(str11))
print(int(True), float(False), str(False))






















