num=int(input("Enter the numbers to find fibonacci series- "))
n1=0
n2=1
count=0
print("Fibonacci Sequence- ")
while(count<num):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count+=1