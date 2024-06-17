input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

starts_with_prefix = input_string.startswith(prefix)
ends_with_suffix = input_string.endswith(suffix)

if starts_with_prefix:
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

if ends_with_suffix:
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")
