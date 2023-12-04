import sys

# Open the input and turn it into lines.
with open(sys.argv[1], 'r') as file:
    original_cards = [line.strip() for line in file]

# Initialize a queue to track cards to be processed, starting with the original set
cards_to_process = [(card, 1) for card in original_cards]  # Tuple format: (card, number of instances)

# Initialize total cards counter
total_cards = 0

# Process each card
while cards_to_process:
    card, instances = cards_to_process.pop(0)
    total_cards += instances  # Add the number of instances of this card

    # Print current card being processed and its instances
    print(f"Processing {card.split(':')[0]} with {instances} instance(s)")

    # Split the line at ':', then split the card into scratch and winning numbers
    _, card_numbers = card.split(':')
    scratch_side, winning_side = card_numbers.split('|')
    scratch_numbers = [int(num) for num in scratch_side.split()]
    winning_numbers = [int(num) for num in winning_side.split()]

    # Count matching numbers
    match_count = sum(num in winning_numbers for num in scratch_numbers)

    # Add subsequent cards based on the number of matches
    current_index = original_cards.index(card)
    for i in range(1, match_count + 1):
        next_card_index = current_index + i
        if next_card_index < len(original_cards):
            next_card = original_cards[next_card_index]
            cards_to_process.append((next_card, instances))  # Add one copy for each instance of the current card

# Print the total number of cards processed
print(f"Total number of cards processed: {total_cards}")
