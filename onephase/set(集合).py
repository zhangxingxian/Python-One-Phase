

# 创建set需要一个list或者tuple或者dict作为输入集合
# 重复元素在set中会被自动过滤

set1 =set([1,2,2,3,4,5,5,6,7,7])
print(set1)
 
set2 = set((1,2,3,4,4,4,5,6,6,7,))
print(set2)

set3 = set({"tom":12, "lilei":13})	# 字典作为输入值时只获取键
set4 = set({12:"tom", 13:"lilei"})
print(set3)
print(set4)


set5 = set([1,2,3])
set5.add(3)	# 添加元素
set5.add(4)
print(set5)
# set5.add([4,5,6])	# set的元素不能是列表，因为列表是可变的
# set5.add({1:"tom", 2:"lilie"})	# set的是元素不能时字典，因为字典是可变的
print(set5)


set6 = set([1,2,3,4,5])	# 插入整个list，tuple，字符串，打碎插入
set6.update([6,7,8])
set6.update((9,10,11))
set6.update("zhang")
print(set6)


set7 = set([1,2,3,4])
set7.remove(2)
print(set7)


set8 = set([1,2,3,4,5,6,7])
for i in set8:
	print(i)

# print(set8[2]) # set没有索引

for index, data in enumerate(set8):
	print(index, data)


set9 = set([1,2,3,4])
set10 = set([3,4,5,6])
a1 = set9 & set10
print(a1)
a2 = set9 | set10
print(a2)
a3 = set9 ^ set10
print(a3)
a4 = set9 - set10
print(a4)

"""
{3, 4}
{1, 2, 3, 4, 5, 6}
{1, 2, 5, 6}
{1, 2}
"""

