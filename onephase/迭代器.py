

from collections import Iterable
from collections import Iterator

# 可迭代对象：可以直接作用于for循环 或 有__iter__()方法的对象统称为可迭代对象（Iterable）.可以用isinstance()去判断一个对象是否是Iterable对象

# 可以直接作用于for循环的数据类型一般分为两种
# 1.集合数据类型 list tuple dict set string
# 2.generator，包括生成器和带yield的generator function

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance("", Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(1, Iterable))


print("*****************************")
# 迭代器：不但可以作用于for循环或有__iter__()方法，还可以被next()函数不断调用并返回下一个值，直到最后跑出一个StopIteration的错误，表示无法继续返回下一个值
# 可以被next()函数调用并不断返回下一个值得对象称为迭代器（Iteratord对象）
# 可以使用isinstance()函数判断一个对象是否是Iterator对象

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((), Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))

l = (x for x in [12,3,4,545,57,4])
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
# print(next(l))	# 当取不出元素时会包StopIteration错误


a = iter([1,2,3,4,5])	# 转成Iterator对象
print(next(a))

print(isinstance(iter([]), Iterator))