d={'even':[2,4,4,6,8,20,30,2,8,10],'odd':[3,1,5,7,9,19,11,3,7,9,9]}
p=d.get('even')
mx=0
sec_mx=0
for i in p:
    if i>mx:
       sec_mx=mx
       mx=i
    elif i>sec_mx and i!=mx:
        sec_mx=i
print("maximum number is :",mx,)
print("second maximum number is :",sec_mx)
       
q=d.get('odd')
mn=q[5]
sec_mn=q[6]
for i in q:
    if i<mn:
        mn=i
    elif i<sec_mn and i!=mn:
         sec_mn=i
print("minimum number is : ",mn)        
print("second minimum number is :",sec_mn)
