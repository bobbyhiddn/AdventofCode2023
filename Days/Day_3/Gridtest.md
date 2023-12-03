# Response

Certainly! To address issue 2, we'll need to create functions to find numbers in all four directions (up, down, left, right) and then extend them to handle diagonal numbers. Since we've already got the horizontal case covered with `find_horizontal_number`, we can create a similar function for the vertical numbers.

Here's how you can modify `Gear.py` to include the vertical search:

```python
# Function to find the full number vertically starting from a given position
def find_vertical_number(grid, row, col):
    number = grid[row][col]
    # Extend upwards
    up = row - 1
    while up >= 0 and grid[up][col].isdigit():
        number = grid[up][col] + number
        up -= 1
    # Extend downwards
    down = row + 1
    while down < len(grid) and grid[down][col].isdigit():
        number += grid[down][col]
        down += 1
    return number

# Modify the check_adjacent function to include vertical checks
def check_adjacent(grid, N, J, found_numbers):
    sum_of_numbers = 0
    adjacent_positions = [
        (N, J-1), (N, J+1),    # Left and Right
        (N-1, J-1), (N-1, J), (N-1, J+1),  # Top row (including diagonals)
        (N+1, J-1), (N+1, J), (N+1, J+1)   # Bottom row (including diagonals)
    ]

    for row, col in adjacent_positions:
        if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
            full_number = ''
            if grid[row][col].isdigit():
                # Horizontal number
                full_number = find_horizontal_number(grid, row, col)
            elif col == J and grid[row][col].isdigit():
                # Vertical number (only check if we're in the same column as the symbol)
                full_number = find_vertical_number(grid, row, col)
            
            # If we found a number, add it to the set and sum
            if full_number and full_number not in found_numbers:
                found_numbers.add(full_number)
                print(f"Found number {full_number} at ({row}, {col})")
                sum_of_numbers += int(full_number)

    return sum_of_numbers
```

Please note that we have added an additional condition when checking for vertical numbers to ensure we only consider the vertical case when we're in the same column as the symbol. This is because the `find_vertical_number` function assumes that you start from a digit, not a symbol.

Now, the `check_adjacent` function will check for both horizontal and vertical numbers adjacent to symbols.

To handle diagonal numbers, you would need to extend the logic further by developing a way to find numbers diagonally. This would be similar to the vertical and horizontal search, except it would search along both rows and columns simultaneously.

As your spellbook grows more complex, be mindful of the possibility of overlapping numbers or those that can be read in multiple directions. Each unique number should be counted only once.