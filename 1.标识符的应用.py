"""
多行注释：三引号
常量： 456, 123 (没有命名直接用), "python"
变量：实际上相当于一个标签，给一个东西作标记代替



"""
# 变量使用 pai是一个变量，里面放的是3.14
pai = "3.14"
print(3.14)
# = :赋值符号，将3.14赋值给pai
car = "法拉利"
print(car)

""""
python命名规范：给变量，函数，类...命名
1.大小写敏感，区分大小写，列如：NAME跟name不一样
注意：学过的Linux区分大小写，而MySQL语法不区分大小写
2.一般情况，变量，函数，对象（变量对象）用小写单词命名
3.见名知意，看见名字就能猜到内容是什么（car，book，a，b，c）
4.不要用易混淆，0和o，1和l
5.不要用关键词，print, ...下边，一定要用会冲突
写的规范：使用字母，数字，下划线
一定注意：不能以数字开头(123car 不允许的)
多个单词之间建议用下划线隔开，ai_class_one= "人工智能1班"
也可以：驼峰命名法
aiClassOne = "人工智能1班"
需要首字母大写，比如类：Pythonstudent
6.Python中单独的下划线_用于表示上次运算的结果

"""
# 导入一个模块，包，库
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']



#  注意：Python关键字是不带括号的，带有编程逻辑功能，如：import导入模块的作用
# print（），带有括号的函数，可以实现某种功能，处理一些事情
# type（），查看数据类型
print(0o1010)