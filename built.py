'''a=3
b=4
print(a*b)
print(min(a,b))
print(max(a,b))

a=[3,5,2,1,1]
print(type(a))
print(len(a))
print(sum(a))
for i in range(len(a)):
    print(a[i])
c=input()
print(c)'''
'''#directory-it is a collection of files.
for i in range(65,91):
    print(chr(i),end=" ")'''

'''a=input()
for i in a:
    print(i,"-",ord(i))'''

'''#fromkeys
a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))
b=dict.fromkeys(a)
print(b)
b=dict.fromkeys(a,"pooja mam")
print(b)
b["c"]="codegnan"
print(b)'''



a="codegnan"
for i in a:
    if i=='c':
        c=dict.fromkeys(i,"codegnan")
    else:
        c.update(dict.fromkeys(i,"pooja mam"))
print(c)


    
