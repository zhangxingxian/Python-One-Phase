# 位运算
print(5 & 7)
print(5 | 7)
print(5 ^ 7)
print(~5)
print(2 << 2)
print(-13 >> 2)

# 逻辑运算
num1 = 10
num2 = 20

if num1 and num2:
	print("*")
print(num1, num2)

# 短路原则	
# exp1 and exp2 and exp3 and ... and expn

num3 = 0
num4 = 1
if num3 or num4:
	print("**")

if not 0:
	print("***")


# 成员运算符
#in：如果在指定的序列中没有找到值返回True,否则返回False
#not in：如果在指定的序列中没有找到值返回True,否则返回False