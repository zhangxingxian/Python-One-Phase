str1 = "sunck is a good man!"
str2 = "sunck is a nine man!"
str3 = "sunck is a handsome man!"
str6 = "sunck is a "
str7 = "good man!"
str8 = str6 + str7
print(str6)
print(str7)
print(str8)
print("-".join(str6))

str9 = "good"
str10 = str9 * 3
print(str10)

str11 = "sunck is a good man! 凯"
print(str11[0])
# str11[0] = "z" 字符串不可变

str13 = "sunck is a good man!"
str15 = str13[6:15]
str16 = str13[:5]
str17 = str13[16:]
print(str17)

str18 = "sunck is a good man!"
print("good" in str18)
print("GOOD" not in str18)


print("sunck is a good man!")
num = 19
str19 = "sunck is a good man!"
f = 10.1234
print("num = %d, str19 = %s f = %.3f" % (num, str19, f))
print("num = %d\nstr19 = %s\nf = %.3f" %(num, str19, f))
print("sunck \\ is")
print('tom is a \'good\' man')
print("tom is a \"good\" man")
print("good\nnine\nhandsome")
print("""
gOOd
nine
handsome""")
print("sunck\tgood")
print(r"\\t\\\\")


# eval(str)
num1 = eval("123")
print(num1)
print(type(num1))
print(len("sunck"))
print("ASDFasdf".lower())
print("ASDFasdf".upper())
print("ASDFasdf".swapcase())
print("sunck iS A gOOd man".capitalize())
print("sunck iS A gOOd man".title())

str25 = "kaige is a good man"
print(str25.center(40,"*"))
print(str25.ljust(40, "%"))
print(str25.rjust(40, "%"))
print(str25.zfill(40))


str29 = "kaige is a very very nice man"
print(str29.count("very", 15 ,len(str29)))

print(str29.find("is")) # 返回第一次出现的下标

print(str29.rfind("very"))

print(str29.index("s")) # 根find()一样 只不过如果str不存在的时候回报错

print(str29.rindex("very"))

str33 = "**********kaige is a nice man********"
print(str33.lstrip("*"))
print(str33.rstrip("*"))
print(str33.strip("*"))


str35 = "zhang-xing-xian is a \ngood man,nice man! "
print(str35.split("-",1)) #返回一个列表 
print(str35.splitlines())
print(str35.replace("-", " ", 1))
print(str35.partition("m")) #保留分割字符

str36 = "a"
print(ord(str36))

str37 = 65
print(chr(str37))
