"""
##set problems
1)WAP to add squares of even numbers into set, where numbers are ranging from 1 to 21.
s=set()
for i in range(1,21):
    if i%2==0:
        s.add(i*i)
print(s)
--------------------------------------
2)WAP to insert 2-tuple into set where, tuple contains (number and square of that number) from the
range(1,21)
s=set()
for i in range(1,21):
    t=(i,i*i)
    s.add(t)
print(s)
-----------------------------------------
3)WAP to find such elements which are present in current set but not in another.
i.e remove common elements from current set.

s1=set(input("Enter set1: "))
s2=set(input("Enter set2: "))
print(s1.difference(s2))#{'h', 'c', 't', 'y'}
------------------------------------------
4)WAP to find element which are not common in both sets.
s1=set(input("Enter set1: "))
s2=set(input("Enter set2: "))
print(s1.symmetric_difference(s2))#{'g', 'y', 'a', 't', 'r', 'm', 'c', 'h'}
----------------------------------------------
5)WAP to find common elements from both sets
s1=set(input("Enter set1: "))
s2=set(input("Enter set2: "))
print(s1.intersection(s2))#{'n', 'i', 'P', 'o'}
-------------------------------------------
6)WAP to combine two sets
s1=set(input("Enter set1: "))
s2=set(input("Enter set2: "))
print(s1.union(s2))#{'o', 't', 'g', 'P', 'n', 'm', 'a', 'c', 'h', 'r', 'i', 'y'}
---------------------------------------
7)WAP to find length of a given set without using 'len' function
s={'g', 'y', 'a', 't', 'r', 'm', 'c', 'h'}
c=0
for i in s:
    c+=1
print(f"Length={c}")
---------------------------------------
8)WAP to find maximum value in a set without using any built-in functions
s={5,10,3,4,6,2,1,9,11,7,8}

c=0#11

for i in s:#i=5,10,3,4,6,2,1,9,11,7,8
    if i>c:
        c=i
print(c)
--------------------------------------------
9)WAP to find minimum value in a set without using any built-in functions

s={5,10,3,4,6,2,1,9,11,7,8}

c=s.pop()
print("Original c=",c)
s.add(c)

for i in s:#i=5,10,3,4,6,2,1,9,11,7,8
    if i<c:
        c=i
print("Min value is",c)
-----------------------------------------
10)WAP to find average of set elements
average=total/len

s={5,10,3,4,6,2,1,9,11,7,8}

c=0
for i in s:
    c+=i

avg=c/len(s)
print(avg)
--------------------------------------
11)#Hackerrank

arr=[1,5,3]
A={3,1}
B={5,7}

hap=0#1

for i in arr:#i=1, 5, 3
    if i in A:
        hap+=1
    elif i in B:
        hap-=1
    else:
        pass
    
print("Happiness=", hap)
-----------------------
list_problems_sagar_nangare_dsp_27.py
"""
