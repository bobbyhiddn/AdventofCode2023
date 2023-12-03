import re

def concatenate_first_and_last_digit(s):
    # Using regular expression to find all numbers in the string
    numbers = re.findall(r'\d+', s)
    if not numbers:
        return None  # No numbers found
    # Take the first digit of the first number and the last digit of the last number
    first_digit = numbers[0][0]
    last_digit = numbers[-1][-1]
    return int(first_digit + last_digit)

# Read jumbled strings from 'Trebuchet.txt'
with open('Trebuchet.txt', 'r') as file:
    jumbled_strings = [line.strip() for line in file]

# Initialize a variable to store the sum of all concatenated numbers
total_sum = 0

# Processing each jumbled string
for jumbled_string in jumbled_strings:
    concatenated_number = concatenate_first_and_last_digit(jumbled_string)
    if concatenated_number is not None:
        print(f"Concatenated number in '{jumbled_string}': {concatenated_number}")
        total_sum += concatenated_number
    else:
        print(f"No numbers found in '{jumbled_string}'")

# Print the total sum
print(f"Total sum of concatenated numbers: {total_sum}")
