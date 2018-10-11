

tuple1 = ()
print(tuple1)
print(type(tuple1))


tuple2 = (1,2,"good",True)
print(tuple2)


tuple3 = (1)
tuple4 = (1,)	# 定义单元素元组
print(type(tuple3))
print(type(tuple4))
print(tuple3)
print(tuple4)


tuple5 = (1,2,3,4,5)
print(tuple5[2])
print(tuple5[-2])


tuple6 = (1,2,3,4,5,[6,7,8])
#tuple6[2] = 300	# 元组不可修改， 但也不是完全不能修改
tuple6[5][2] = 800
print(tuple6)


tuple7 = (0,1,2,3)
del tuple7
#print(tuple7)	del 删除后就没有这个元组了


tuple8 = (1,2,3)
tuple9 = (4,5,6)
tuple10 = tuple8 + tuple9
print(tuple10)


tuple11 = (1,2,3)
print(tuple11 * 3)


tuple12 = (1,2,3)
print(2 in tuple12)


tuple13 = (1,2,3,4,5,6,7,8,9,0)
print(tuple13[3:8])
print(tuple13[:3])
print(tuple13[3:]) 


tuple14 = ((1,2,3),(4,5,6),(7,8,9))
print(tuple14[1][1])


tuple15 = (1,2,3,4)
print(len(tuple15))
print(min(tuple15))
print(max(tuple15))


list = [1,2,3]
tuple16 = tuple(list)
print(tuple16)


for i in (1,2,3,4,5):
	print(i)