str1=input("Enter the string 1- ")
str2=input("Enter the string 2- ")
str1=str1.replace(" ","")
str2=str2.replace(" ","")
str1=str1.lower()
str2=str2.lower()
if(sorted(str1)==sorted(str2)):
    print(str1," and ",str2," are anagrams.")
else:
    print(str1," and",str2," are not anagrams.")