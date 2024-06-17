lst=[]
n=int(input("Enter the number of elements in the list- "))
for i in range(0,n):
    ele=int(input(f"Enter the element{i+1}: "))
    lst.append(ele)
print("Minimum element of the list is= ",min(lst))
print("Maximum element of the list is= ",max(lst))