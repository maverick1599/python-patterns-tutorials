# Basic Number Sorting

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

order = input("Do you want to sort the list in ascending or descending order? (a/d): ").lower()

if order == 'a':
    sorted_numbers = sorted(numbers)
    print(f"Sorted numbers in ascending order: {sorted_numbers}")
elif order == 'd':
    sorted_numbers = sorted(numbers, reverse=True)
    print(f"Sorted numbers in descending order: {sorted_numbers}")
else:
    print("Invalid choice! Please choose 'a' for ascending or 'd' for descending.")
