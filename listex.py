l=[1,2,3,4,5]
print(l)
mx=0
for i in l:
    if i>mx:
        mx=i
print(mx)

mn=l[0]
for i in l:
    if i<mn:
        mn=i
        
length=len(l)-1
temp=l[0]
l[0]=l[length]
l[length]=temp
print(l)


total=0
for i in l:
    total=total+i
avg=total/len(l)
print(avg)

d={1:'one',2:'two',3:'three',5:'five',4:'four','name':'mp'}
print(d)


s={7,8,2,7,3,9,7}
print(s)
