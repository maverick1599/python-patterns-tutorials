# Find Largest Number in a List

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

largest_number = max(numbers)

print(f"The largest number in the list is {largest_number}.")
