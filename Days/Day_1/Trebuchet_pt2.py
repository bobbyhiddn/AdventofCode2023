import re

# Mapping of spelled out numbers to digits
number_words = {
    "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def find_and_convert_numbers(s):
    # Extract words from the string that match our number_words keys
    words = re.findall(r'\b(' + '|'.join(number_words.keys()) + r')\b', s, flags=re.IGNORECASE)

    # Convert each word to its corresponding digit and join them together
    number_string = ''.join(number_words[word.lower()] for word in words)

    # Return the number string if it's not empty, else None
    return number_string if number_string else None

def concatenate_first_and_last_digit(s):
    number_string = find_and_convert_numbers(s)
    if not number_string:
        return None  # No numbers found
    # Take the first and last digit
    first_digit = number_string[0]
    last_digit = number_string[-1]
    return int(first_digit + last_digit)

# Read jumbled strings from 'Trebuchet.txt'
with open('Trebuchet.bk.txt', 'r') as file:
    jumbled_strings = [line.strip() for line in file]

# Create a new list of concatenated numbers
concatenated_numbers = [concatenate_first_and_last_digit(s) for s in jumbled_strings if concatenate_first_and_last_digit(s) is not None]

# Process and print each concatenated number
for jumbled_string, concatenated_number in zip(jumbled_strings, concatenated_numbers):
    print(f"Concatenated number in '{jumbled_string}': {concatenated_number}")

# Calculate and print the total sum
total_sum = sum(concatenated_numbers)
print(f"Total sum of concatenated numbers: {total_sum}")

