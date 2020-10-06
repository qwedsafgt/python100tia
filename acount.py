one=int(input("请输入一个正整数"))
otherone=int(input("请再输入一个正整数"))
if one>otherone:
    one,otherone=otherone,one
for a in (one,0,-1):#这里为什么不能输0
    print(one)
    print(one*otherone//a)
