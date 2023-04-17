# 变量赋值
school = "河南艺术职业学院"
print(school)

# 2.多个变量一起赋值
a = 1
b = 4
c = 9
print(a,b,c)
x, y, z, = 10, 19, 22
print(x,y,z)
o,p,q = "嗯嗯嗯",33333,88888
print(o,p,q)
# 多个变量赋相同的值
a1 = 9
b1 =9
c1 =9
a1,b1,c1 =9,9,9
print(a1,b1,c1)
# 用=号连接
a2 = b2 = c2 = 99
print(a2,b2,c2)
# 变量进行数值交换
# 通过第三个变量进行数值交换
rmb = 100
dollor = 15.84
j = dollor     # j =  dollor  = 15.84
print("j",j)
dollor = rmb
rmb = j
print(rmb,dollor)
# Python可以直接交换
rmb,dollor = dollor,rmb
print(rmb,dollor)
# 练习： m = "吕布" n = "赵云" u = "关羽"
# n = "吕布" m = "关羽" u = "赵云"
m = "吕布"
n = "赵云"
u = "关羽"
print (m,n,u)
m,n,u = n,u,m
print(m,n,u)

















