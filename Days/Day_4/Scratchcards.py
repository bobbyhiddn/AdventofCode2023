import sys

# Open the input and turn it into lines.
with open(sys.argv[1], 'r') as file:
    cards = [line.strip() for line in file]

# Initialize total score
total_score = 0

# Process each card
for card in cards:
    # Split the line at ':', then split the card into scratch and winning numbers
    _, card_numbers = card.split(':')
    scratch_side, winning_side = card_numbers.split('|')
    scratch_numbers = [int(num) for num in scratch_side.split()]
    winning_numbers = [int(num) for num in winning_side.split()]

    # Initialize score for this card
    score = 0

    # Update score for each matching number
    for num in scratch_numbers:
        if num in winning_numbers:
            score = 1 if score == 0 else score * 2

    # Add the score of this card to the total score
    total_score += score

# Print the total score
print(total_score)
