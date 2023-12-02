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

def is_game_possible(game_info, max_red, max_green, max_blue):
    for subset in game_info:
        if subset['red'] > max_red or subset['green'] > max_green or subset['blue'] > max_blue:
            return False
    return True

def analyze_games_from_file(file_path, max_red, max_green, max_blue):
    possible_games = []
    
    with open(file_path, 'r') as file:
        for line in file:
            parsed_game = parse_game_data(line.strip())
            if parsed_game and is_game_possible(parsed_game[1], max_red, max_green, max_blue):
                possible_games.append(parsed_game[0])
    
    return sum(possible_games)

# File path to your data
file_path = 'Conundrum_Data.txt'

max_red = 12
max_green = 13
max_blue = 14

# Calculate the sum of IDs of possible games
result = analyze_games_from_file(file_path, max_red, max_green, max_blue)
print("Sum of IDs of possible games:", result)
