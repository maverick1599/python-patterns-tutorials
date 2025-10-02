# Palindrome Checker

word = input("Enter a word: ").lower()

if word == word[::-1]:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")
