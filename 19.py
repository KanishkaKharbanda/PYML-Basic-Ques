str=input("Enter the string: ")
str_without_punctuation=""
punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for char in str:
    if char not in punctuation:
        str_without_punctuation+=char
print("String without punctuation:: ",str_without_punctuation)