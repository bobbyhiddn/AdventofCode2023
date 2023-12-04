import sys

# Open the input and turn it into lines.
with open(sys.argv[1], 'r') as file:
    cards = [line.strip() for line in file]

# First pass: count winning numbers for each card
winning_counts = []
for card in cards:
    _, card_numbers = card.split(':')
    scratch_side, winning_side = card_numbers.split('|')
    scratch_numbers = [int(num) for num in scratch_side.split()]
    winning_numbers = [int(num) for num in winning_side.split()]
    
    winning_counts.append(sum(num in winning_numbers for num in scratch_numbers))

# Second pass: calculate total cards
total_cards = [1] * len(cards)  # Start with one instance of each card
for i, count in enumerate(winning_counts):
    for j in range(1, count + 1):
        if i + j < len(cards):
            total_cards[i + j] += total_cards[i]

# Final calculation: sum up all cards
total = sum(total_cards)

# Print the total number of cards processed
print(total)
