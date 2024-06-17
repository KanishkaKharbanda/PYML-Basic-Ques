a=10
b=17
c=20
#Code to find maximum and minimum of three numbers
if(a>b and a>c):
    print(a," (a) is the maximum number")
elif(b>a and b>c):
    print(b," (b) is the maximum number")
else:
    print(c," (c) is the maximum number")

if(a<b and a<c):
    print(a," (a) is the minimum number")
elif(b<a and b<c):
    print(b," (b) is the minimum number")
else:
    print(c," (c) is the minimum number")
#Code to check which is even number
if(a%2==0):
    print(a," (a) is an even number")
elif(b%2==0):
    print(b," (b) is an even number")
elif(c%2==0):
    print(c," (c) is an even number")
else:
    print("No number is an even number")
#Code to swap the values of a and b without using third variable
print("Value of a- ",a)
print("Value of b- ",b)
a=a+b
b=a-b
a=a-b
print("After Swapping:: ")
print("Value of a- ",a)
print("Value of b- ",b)