# print(): 函数，输出打印

# 1.print()输出变量
print("上衫绘梨衣")
print(5233331)
name = "蔡少芬"
print(name)
# 打印多个变量
a,b,c  = 80,90,60
print(a,b,c)
# 3.print():参数end，默认是 \n 是换行符
print("去掉换行符",end = "!")
print("不换行了",end= "--python")
print("白日依山尽\n黄河入海流")
"""
\n: 叫换行符，这种前边带着\ 是转义符
\t: 制表符，是一个tab键，默认四个空格
\\:就是一个\
"""
print("春眠不觉晓\t处处闻啼鸟\t夜来风雨声\t花落知多少")
print("\n是一个换行符")
# 利用\ 将转义字符在转译成普通字符
print("\\n是一个换行符")
# 还可以在字符串前加上r，这样不会转义
print(r"\n是一个换行符")
# "和" 也是具有编程逻辑
print("鲁迅说'世上本没有路'")
print("周总理说\"为中华崛起而读书\"")
print("""  
 
 三个引号时多行注释，也是字符串
 这里就可以"使用单双引号"
 """)
print(r'''
         悯农 \n
         锄禾日当午，汗滴禾下土
         谁知盘中餐，粒粒皆辛苦

''')
print("\103","\x42")

# input(): 函数，接收键盘输入的内容
name = input("请输入一个名字：")
print(name)

number = input("请输入您的银行卡余额:" )
print(number)
print(type(number))
print(int(number),type(int(number)))
