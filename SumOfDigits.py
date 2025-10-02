# Sum of Digits

num = input("Enter a number: ")

# Convert each character in the string to an integer and calculate the sum
sum_digits = sum(int(digit) for digit in num)

print(f"The sum of the digits of {num} is {sum_digits}.")
