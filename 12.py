num=int(input("Enter the number to calculate sum of its digit: "))
sum=0
while(num>0):
    dig=num%10
    sum+=dig
    num//=10
print("Sum of digits are: ",sum)