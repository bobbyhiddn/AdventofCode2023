# Define the jumbled strings and number words
jumbled_strings = [
    "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four",
    "4nineeightseven2", "zoneight234", "7pqrstsixteen"
]

number_words = {
    "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

# Initialize an array to store the couplets
couplets = []

# Replace spelled-out numbers with digits in each string and find first and last digit
for jumbled_string in jumbled_strings:
    for number_word, digit in number_words.items():
        jumbled_string = jumbled_string.replace(number_word, digit)

    # Extract digits from the string
    digits = [char for char in jumbled_string if char.isdigit()]
    if digits:
        first_digit = digits[0]
        last_digit = digits[-1]
        number_couple = int(first_digit + last_digit)
        couplets.append(number_couple)

# Sum all the couplets
couplets_sum = sum(couplets)

print(couplets_sum)
