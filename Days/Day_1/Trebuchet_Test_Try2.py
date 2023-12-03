
# Define the mapping of number words to their numerical equivalents
number_words = {
    "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

# Read jumbled strings from a file (assuming the file contains one string per line)
jumbled_strings = [
    "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four",
    "4nineeightseven2", "zoneight234", "7pqrstsixteen"
]

# Identify number words in each jumbled string and print the result
for jumbled_string in jumbled_strings:
    for number_word in number_words.keys():
        if number_word in jumbled_string:
            print(f"Found '{number_word}' in '{jumbled_string}'")

# So that properly identified all the number words in the strings, now we need to turn them into digits in their proper order

# # Replace spelled-out numbers with their digit equivalents
# for number_word, digit in number_words.items():
#     for jumbled_string in jumbled_strings:
#         jumbled_string = jumbled_string.replace(number_word, digit)
#         print(jumbled_string)

# That did replace the number words with their digit equivalents, but because it did it in order 1-9, so for cases like eightwothree, it replaced the two first, so that it became eigh2hree. This makes it so that the fully digitized string cannot be properly parsed. 

