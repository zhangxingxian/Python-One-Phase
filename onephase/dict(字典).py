

dict1 = {"tom":12,"lilei":13}
print(dict1["tom"])
print(dict1.get("tom"))
print(dict1.get("sucnk",))
print(dict1.get("sucnk","没有这个键"))


dict1["zhang"] = 20
print(dict1)



dict1.pop("tom")	# 字典的删除要指定删除的键
print(dict1)


for key in dict1:
	print(key, dict1[key])


for value in dict1.values():
	print(value)


for k, v in dict1.items():
	print(k, v)


for i, k in enumerate(dict1):	# 枚举取的键
	print(i, k)




# tuple和list比较
# 1.查找和插入速度极快，不会随着key-value的增加而变慢
# 2.需要占用大量内存，内存浪费多


# list
# 1.查找和插入的速度随着数据量的增多而减慢
# 2.占用空间小，浪费内存小
#粘贴的到仓库没有提交的选择