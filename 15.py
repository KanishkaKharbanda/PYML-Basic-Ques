import csv

def read_and_print_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

file_path = input("Enter the path to the CSV file: ")
read_and_print_csv(file_path)
