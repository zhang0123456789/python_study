
'''等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,
等号（=）运算符右边是存储在变量中的值。'''
# counter=100  #整形变量
# miles=1000.0  #浮点型变量
# name='runoob'  #字符串
# print(counter)
# print(miles)
# print(name)

#创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
#多个变量赋值
# a=b=c=1
# #多个对象指定多个变量
# a, b, c = 1, 2, "runoob"

#六种标准的数据类型：
'''number(数字)、string(字符串)、list(列表)、
tuple(元组)、set(集合)、dictionary(字典)'''

#Python3 的六个标准数据类型中：
'''不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。'''

#内置的 type() 函数可以用来查询变量所指的对象类型。
# a,b,c,d=20,5.5,True,4+3j
# print(type(a),type(b),type(c),type(d))

#当你指定一个值时，Number 对象就会被创建：
# var1 = 1
# var2 = 10

#您也可以使用del语句删除一些对象引用。
'''del语句的语法是：del var1[,var2[,var3[....,varN]]]'''

#您可以通过使用del语句删除单个或多个对象。例如：
# del var
# del var_a, var_b

# a=5+4   #加法
# print(a)

# a=4.3-2    #减法
# print(a)

# a=3*7     #乘法
# print(a)

# a=2/4   #除法，得到一个浮点数
# print(a)

# a=2//4     #除法。得到一个整数
# print(a)

# a=17%3         #取余
# print(a)

# a=2**5   #乘方
# print(a)

'''1、一个变量可以通过赋值指向不同类型的对象。
2、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
3、在混合计算时，Python会把整型转换成为浮点数。'''

'''Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。'''

#字符串的截取语法格式：  变量：[头下标:尾下标]
# str='Runoob'
# print (str)          # 输出字符串
# print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
# print (str[0])       # 输出字符串第一个字符
# print (str[2:5])     # 输出从第三个开始到第五个的字符
# print (str[2:])      # 输出从第三个开始的后的所有字符
# print (str * 2)      # 输出字符串两次
# print (str + "TEST") # 连接字符串

'''Python 使用反斜杠(\)转义特殊字符'''
# print('Ru\noob')

'''如果你不想让反斜杠发生转义，
可以在字符串前面添加一个 r，表示原始字符串：'''
# print(r'Ru\noob')

'''Python 没有单独的字符类型，一个字符就是长度为1的字符串。'''
# word='python'
# print(word[0],word[5])
# print(word[-1],word[-6])

'''1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。'''

'''列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，
列表被截取后返回一个包含所需元素的新列表
列表的截取语法格式：  变量：[头下标:尾下标]'''

# list = ['abcd', 786, 2.23, 'runoob', 70.2]
# tinylist = [123, 'runoob']

# print(list)  # 输出完整列表
# print(list[0])  # 输出列表第一个元素
# print(list[1:3])  # 从第二个开始输出到第三个元素
# print(list[2:])  # 输出从第三个元素开始的所有元素
# print(tinylist * 2)  # 输出两次列表
# print(list + tinylist)  # 连接列表

'''与Python字符串不一样的是，列表中的元素是可以改变的：'''
# a=[1,2,3,4,5,6]
# a[0]=9
# print(a)

# a=[1,2,3,4,5,6]
# a[2:5]=13,14,15
# print(a)

'''注意：
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。'''

'''元组（tuple）与列表类似，不同之处在于元组的元素不能修改。
元组写在小括号 () 里，元素之间用逗号隔开。'''
# tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
# tinytuple = (123, 'runoob')
#
# print(tuple)  # 输出完整元组
# print(tuple[0])  # 输出元组的第一个元素
# print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
# print(tuple[2:])  # 输出从第三个元素开始的所有元素
# print(tinytuple * 2)  # 输出两次元组
# print(tuple + tinytuple)  # 连接元组

# tup = (1, 2, 3, 4, 5, 6)
# print(tup[0])
# print(tup[1:5])

'''虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：'''
# tup1=() #空元组
#
# tup2=(20,)#一个元素，需要在后面添加逗号,否则括号当运算符
# print(type(tup2))

'''注意：
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含0或1个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。'''


'''集合（set）是由一个或数个形态各异的大小整体组成的，
构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。'''

# 集合
# 成员测试
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)  # 输出集合，重复的元素被自动去掉
# if 'Rose' in student :
#     print('Rose 在集合中')
# else :
#     print('Rose 不在集合中')

# set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a - b)  # a和b的差集
# print(a | b)  # a和b的并集
# print(a & b)  # a和b的交集
# print(a ^ b)  # a和b中不同时存在的元素

'''列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。'''
# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
# tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
#
# print(dict['one'])  # 输出键为 'one' 的值
# print(dict[2])  # 输出键为 2 的值
# print(tinydict)  # 输出完整的字典
# print(tinydict.keys())  # 输出所有键
# print(tinydict.values())  # 输出所有值

'''构造函数 dict() 可以直接从键值对序列中构建字典如下：
注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。'''
# a=dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# print(a)
# b=dict(Runoob=1, Google=2, Taobao=3)
# print(b)

'''oct() 函数将一个整数转换成8进制字符串。'''
# a=oct(10)
# print(a)
# b=oct(20)
# print(b)

'''hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。返回16进制数，
以字符串形式表示。'''
# a=hex(255)
# print(a)
# print(type(a))
# b=hex(12)
# print(b)
# print(type(b))

'''dict() 函数用于创建一个字典。
dict 语法：     **kwargs -- 关键字、mapping -- 元素的容器、iterable -- 可迭代对象。
返回一个字典。
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)'''

# m=dict(a='a', b='b', t='t')     # 传入关键字
# print(m)
# n=dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
# print(n)
# p=dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
# print(p)

'''tuple 函数将列表转换为元组。。tuple 的语法:tuple( seq )seq -- 要转换为元组的序列。'''
# list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# tuple1=tuple(list1)
# print(tuple1)

'''list() 方法用于将元组或字符串转换为列表。list()方法语法:list()方法语法
注：元组与列表是非常类似的，区别在于元组的元素值不能修改，ist -- 要转换为列表的元组或字符串。
元组是放在括号中，列表是放于方括号中。'''

# aTuple = (123, 'Google', 'Runoob', 'Taobao')
# list1 = list(aTuple)
# print ("列表元素 : ", list1)
#
# str="Hello World"
# list2=list(str)
# print ("列表元素 : ", list2)

'''str() 函数将对象转化为适于人阅读的形式。语法：class str(object='')'''
dict = {'runoob': 'runoob.com', 'google': 'google.com'};
print(str(dict))