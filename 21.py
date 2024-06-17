lst=[]
n=int(input("Enter the number of elements in the list- "))
for i in range(0,n):
    ele=input(f"Enter the element{i+1}: ")
    lst.append(ele)
print("Count the occurence of 'a' in the list is-", lst.count('a'))