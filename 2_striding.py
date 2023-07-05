s="Python"

print(s[0:5:1])
print("*",s[-6:-1:1])
print(s[6:0:-1])

print(s[5:0:-1])

print(s[::-1])

print(s[::])

#positve Striding
#i.both start an end is given

print("i.both start an end is given")

print(s[0:5:1])

print(s[0:6:1])

print(s[0:6:2])#odd places

print(s[1:6:2])#even places

print("*",s[-6:-1:1])

print(s[-1:-6:1])#empty output

print(s[-10:-1:1])

print(s[-6:0:1])#empty output


#ii.only start is given

print("ii.only start is given")

print(s[0::1])

print(s[2::3])

print(s[5::1])

print(s[6::1])#empty

print(s[-6::1])

print(s[-1::1])

print(s[-6::1])


"""

#iii.only end is given+

print("iii.only end is given")

print(s[:6:1])

print(s[:5:1])

print(s[:1:1])
"""
