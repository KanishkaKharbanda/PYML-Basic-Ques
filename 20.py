lst=[]
n=int(input("Enter the number of elements in the list- "))
for i in range(0,n):
    ele=int(input(f"Enter the element{i+1}: "))
    lst.append(ele)
total=sum(lst)
print("Sum of elements of the list= ",total)