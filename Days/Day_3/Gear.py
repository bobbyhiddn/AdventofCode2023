import sys

# Function to find the full number horizontally starting from a given position
def find_horizontal_number(grid, row, col):
    # Construct the number to the left
    number_left = ''
    left = col
    while left >= 0 and grid[row][left].isdigit():
        number_left = grid[row][left] + number_left
        left -= 1

    # Construct the number to the right
    number_right = ''
    right = col + 1
    while right < len(grid[row]) and grid[row][right].isdigit():
        number_right += grid[row][right]
        right += 1

    # Combine left and right parts
    return number_left + number_right if number_left else number_right

# Function to check and return the sum of numbers adjacent to a given symbol location
def check_adjacent(grid, N, J, found_numbers):
    sum_of_numbers = 0
    adjacent_positions = [
        (N, J-1), (N, J+1),    # Left and Right
        (N-1, J-1), (N-1, J), (N-1, J+1),  # Top row (includes diagonals)
        (N+1, J-1), (N+1, J), (N+1, J+1)   # Bottom row (includes diagonals)
    ]

    for row, col in adjacent_positions:
        if 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col].isdigit():
            horizontal_number = find_horizontal_number(grid, row, col)
            # Find the starting position of the full number
            start_col = col
            while start_col > 0 and grid[row][start_col - 1].isdigit():
                start_col -= 1

            number_location = (horizontal_number, row, start_col)
            if number_location not in found_numbers:
                found_numbers.add(number_location)
                print(f"Found number {horizontal_number} at ({row}, {col})")
                sum_of_numbers += int(horizontal_number)

    return sum_of_numbers

# Read the grid from the file and separate it into lines
with open(sys.argv[1], 'r') as file:
    grid = [line.strip() for line in file]

symbols = ['*', '#', '+', '$', '/', '&', '@', '!', '%', '=', '-']
found_numbers = set()
total_sum = 0

for N in range(len(grid)):
    for J in range(len(grid[N])):
        if grid[N][J] in symbols:
            total_sum += check_adjacent(grid, N, J, found_numbers)

print("Total sum of all found numbers:", total_sum)
