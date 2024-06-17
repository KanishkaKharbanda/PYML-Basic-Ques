str=input("Enter the string:: ")
freq_dict={}
for char in str:
    if char in freq_dict:
        freq_dict[char]+=1
    else:
        freq_dict[char]=1
print(freq_dict)
