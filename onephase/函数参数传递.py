

# 值传递：传递的是不可变类型
# string tuple number 是不可变的类型

def func1(num):
	print(id(num))
	num = 10
	print(id(num))

temp = 20
print(id(temp))
func1(temp)
print(temp)


# 引用传递：传递的可变类型
# list dict set 是可变的

def func2(lis):
	lis[0] = 100
li = [1,2,3,4,5]
func2(li)
print(li)


a = 10
b = 10
b = 40
print(id(a), id(b))

c = 20
d = 30
print(id(c), id(d))
d = c
print(id(c), id(d))


# 关键字参数
# 概念：允许函数调用时参数的顺序与定义时不一致

def myPrint(str, age):
	print(str, age)

myPrint(age = 18, str = "sunck is a good man!")


# 默认参数
# 调用函数时，如果没有传递参数，则使用默认参数
# 以要用的默认参数，最好将默认参数放到最后

def myPrint1(str, age = 18):
	print(str, age)

myPrint1("good")


# 不定长参数
# 概念：能处理比定义时更多的参数
# 加了星号（*）的变量存放所有未命名的变量参数，如果在函数调用的时候没有指定参数，它就是一个空元组

def func(name, *args):
	print(name)
	print(type(args))
	for x in args:
		print(x)

func("sunck", "is", "a", "good", "man")


def mySum(*l):
	sum = 0
	for i in l:
		sum += i
	return sum

print(mySum(1,2,3,4,5,6,7,8,9))


# **代表键值对的参数字典，和*所代表的意义类似

def func2(**kwargs):
	print(kwargs)
	print(type(kwargs))

func2(x=1, y=2, z=3)