import re
import sys

# Mapping of spelled out numbers to digits
number_words = {
    "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def find_and_convert_numbers(s):
    # Dictionary to hold the presence of each number word
    number_presence = {number_word: False for number_word in number_words.keys()}
    
    # List to store the order of numbers found
    number_order = []

    # Check for each number word in the string
    for number_word in number_words.keys():
        if number_word in s.lower():
            number_presence[number_word] = True
            # Find all occurrences and add their start position and corresponding digit to number_order
            for match in re.finditer(number_word, s, flags=re.IGNORECASE):
                number_order.append((match.start(), number_words[number_word]))
    
    # Add actual numerical digits from the string
    for match in re.finditer(r'\d', s):
        number_order.append((match.start(), match.group()))

    # Sort the number_order list based on appearance in the string
    number_order.sort(key=lambda x: x[0])

    # Create the final number string
    number_string = ''.join(digit for _, digit in number_order)

    # Display the presence of each number word and the created string
    print(f"Presence in '{s}': {number_presence}")
    print(f"Converted '{s}' to '{number_string}'")

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
with open(sys.argv[1], 'r') as file:
    jumbled_strings = [line.strip() for line in file]

# Create a new list of concatenated numbers
concatenated_numbers = [concatenate_first_and_last_digit(s) for s in jumbled_strings if concatenate_first_and_last_digit(s) is not None]

# Process and print each concatenated number
for jumbled_string, concatenated_number in zip(jumbled_strings, concatenated_numbers):
    print(f"Concatenated number in '{jumbled_string}': {concatenated_number}")

# Calculate and print the total sum
total_sum = sum(concatenated_numbers)
print(f"Total sum of concatenated numbers: {total_sum}")

