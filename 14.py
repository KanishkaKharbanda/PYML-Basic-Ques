def read_multiple_lines():
    print("Enter multiple lines of text (press Enter on an empty line to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines

user_lines = read_multiple_lines()

print("\nYou entered:")
for line in user_lines:
    print(line)
