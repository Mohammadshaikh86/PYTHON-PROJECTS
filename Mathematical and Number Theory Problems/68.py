def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if 0 <= num < 10:
        return units[num]
    elif 10 <= num < 20:
        return teens[num - 10]
    elif 20 <= num < 100:
        return tens[num // 10] + (" " + units[num % 10] if num % 10 != 0 else "")
    elif 100 <= num < 1000:
        return units[num // 100] + " hundred" + (" and " + number_to_words(num % 100) if num % 100 != 0 else "")
    else:
        return "Number out of range (0-999)"

number = int(input("Enter a number (0-999) to convert to words: "))
words = number_to_words(number)
print(f"{number} in words: {words}")
