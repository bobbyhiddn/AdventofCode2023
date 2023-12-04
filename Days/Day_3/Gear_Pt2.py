import sys

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

    return number_left + number_right if number_left else number_right

def find_gear_ratios(grid):
    gear_ratios_sum = 0

    for N in range(len(grid)):
        for J in range(len(grid[N])):
            if grid[N][J] == '*':  # Check for gears
                adjacent_numbers = []
                adjacent_positions = [
                    (N, J-1), (N, J+1),    # Left and Right
                    (N-1, J-1), (N-1, J), (N-1, J+1),  # Top row (includes diagonals)
                    (N+1, J-1), (N+1, J), (N+1, J+1)   # Bottom row (includes diagonals)
                ]

                for row, col in adjacent_positions:
                    if 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col].isdigit():
                        horizontal_number = find_horizontal_number(grid, row, col)
                        if horizontal_number not in adjacent_numbers:
                            adjacent_numbers.append(horizontal_number)

                if len(adjacent_numbers) == 2:
                    gear_ratio = int(adjacent_numbers[0]) * int(adjacent_numbers[1])
                    gear_ratios_sum += gear_ratio

    return gear_ratios_sum

# Read the grid from the file and separate it into lines
with open(sys.argv[1], 'r') as file:
    grid = [line.strip() for line in file]

total_gear_ratios = find_gear_ratios(grid)
print("Total sum of all gear ratios:", total_gear_ratios)
