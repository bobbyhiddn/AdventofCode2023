grid = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# Convert the grid into a 2D array
grid_array = [list(line) for line in grid.strip().split('\n')]

print(grid_array)

# Function to find positions of symbols and numbers
def find_positions(grid):
    symbols = ['*', '#', '+', '$']
    symbol_positions = {}
    number_positions = []

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in symbols:
                if cell not in symbol_positions:
                    symbol_positions[cell] = []
                symbol_positions[cell].append((i, j))
            elif cell.isdigit():
                number_positions.append((int(cell), (i, j)))

    return symbol_positions, number_positions

symbol_positions, number_positions = find_positions(grid_array)

# Example of how to use the positions to compare
# This part depends on your specific needs
for number, num_pos in number_positions:
    for symbol, symbol_pos_list in symbol_positions.items():
        for symbol_pos in symbol_pos_list:
            if num_pos[0] < symbol_pos[0]:  # number is in a higher row
                print(f"Number {number} is above symbol {symbol}")
            # Add more conditions here based on your requirements
