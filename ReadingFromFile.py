# Reading from a File

file_name = input("Enter the file name to read from (e.g., file.txt): ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("\nFile Content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
