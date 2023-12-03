import re

def parse_game_data(game_string):
    game_pattern = r"Game (\d+): (.+)"
    subset_pattern = r"(\d+) (red|green|blue)"
    
    match = re.match(game_pattern, game_string)
    if not match:
        return None

    game_id = int(match.group(1))
    subsets_str = match.group(2).split(';')
    
    subsets = []
    for subset in subsets_str:
        colors = {'red': 0, 'green': 0, 'blue': 0}
        for number, color in re.findall(subset_pattern, subset):
            colors[color] += int(number)
        subsets.append(colors)
    
    return game_id, subsets

def calculate_game_power(game_info):
    max_red = max_green = max_blue = 0

    for subset in game_info:
        max_red = max(max_red, subset['red'])
        max_green = max(max_green, subset['green'])
        max_blue = max(max_blue, subset['blue'])

    return max_red * max_green * max_blue

def analyze_games_for_power(file_path):
    game_power_sum = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            parsed_game = parse_game_data(line.strip())
            if parsed_game:
                game_power = calculate_game_power(parsed_game[1])
                game_power_sum += game_power
    
    return game_power_sum

# File path to your data
file_path = 'Conundrum_Data.txt'

# Calculate the sum of the powers of possible games
result = analyze_games_for_power(file_path)
print("Sum of the powers of possible games:", result)
