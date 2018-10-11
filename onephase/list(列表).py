list1 = []
print(list1)


list2 = [1,2,3,4,5,6,7,8,9,0]
index = 0
sum = 0
while index < 10:
	sum += list2[index]
	index += 1

	if index == 10:
		print(sum)
		print("平均数%f" % (sum/10))


list3 = [1,2,3,4]
print(list3[2])

list3[3] = 400
print(list3) 


list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6
print(list7)


list8 = [1,2,3]
print(list8 * 3)


list9 = [1,2,3,4,5]
print(2 in list9)
print(9 not in list9)


list11 = [[1,2,3], [4,5,6], [7,8,9]]
print(list11[1][1])


list12 = [1,2,3]
list12.append(4)
list12.append([5,6,7])
print(list12)


list14 = [1,2,3]
list14.extend([4,5,6])
print(list14)


list14 = [1,2,3,4]
list14.insert(0,100)
list14.insert(0,[9,8])
print(list14)


list15 = [1,2,3,4,5]
list15.pop()
print(list15)
list15.pop(2)
print(list15)	#返回删除的元素


list17 = [1,2,1,3,2,4]
list17.remove(1)
print(list17)


list18 = [1,2,3]
list18.clear()
print(list18)


list19 = [1,4,5,2,5,7,4]
index19 = list19.index(2)
index20 = list19.index(2, 1, 5)
print(index19,index20)


list21 = [1,2,43,5,6,7]
print(len(list21))


list22 = [1,2,3,4,5,6,7,8,9]
print(min(list22))
print(max(list22))


list23 = [1,2,4,3,3,6,3,45,6,3,7,7]
print(list23.count(3))

num24 = 0
all = list23.count(3)
while num24 < all:
	list23.remove(3)
	num24 += 1
print(list23)


list25 = [1,2,3,4,5]
list25.reverse()	# 倒序
print(list25)


list26 = [1,65,3,6,7,4,]
list26.sort()	# 升序
print(list26)


list27 = [1,2,3,4,5] # 浅拷贝 引用拷贝
list28 = list27
list28[1] = 200
print(list27)
print(list28)
print(id(list27))
print(id(list28))


list29 = [1,2,3,4,5,6]	# 深拷贝 内存拷贝
list30 = list29.copy()
list30[1] = 200
print(list29)
print(list30)
print(id(list29))
print(id(list30))

