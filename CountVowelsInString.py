# Count Vowels in a String

string = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = sum(1 for char in string if char in vowels)

print(f"The number of vowels in '{string}' is {vowel_count}.")
