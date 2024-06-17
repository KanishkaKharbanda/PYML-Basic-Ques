def write_string_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

input_string = input("Enter a string to write to the file: ")
file_path = 'output.txt' 

write_string_to_file(file_path, input_string)
print(f"The string has been written to {file_path}")
