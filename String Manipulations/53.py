def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Input a string from the user
input_string = input("Enter a string to count vowels: ")

# Count vowels
vowel_count = count_vowels(input_string)

print(f"The string contains {vowel_count} vowels.")
