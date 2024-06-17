def copy_file_contents(source_file_path, destination_file_path):
    try:
        with open(source_file_path, 'r') as source_file:
            contents = source_file.read()

        with open(destination_file_path, 'w') as destination_file:
            destination_file.write(contents)

        print(f"Contents copied from {source_file_path} to {destination_file_path} successfully.")
    except FileNotFoundError:
        print(f"The file {source_file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading from or writing to the file.")

source_file_path = input("Enter the path to the source file: ")
destination_file_path = input("Enter the path to the destination file: ")
copy_file_contents(source_file_path, destination_file_path)
