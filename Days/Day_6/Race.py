# 1. Read in the input file
# 2. Parse the input file into a list of tuples (time, distance)
# 3. tuple[0] = race_time
#    tuple[1] = record_distance
# 4. For each tuple, calculate the distance traveled:
    
#     for i in range(race_time)
#         distance += i
#         if distance > record_distance:
#             add distance to list of possible records

# 5. If the distance traveled is greater than record_distance, add the distance held to the list of possible records.
# 6. Multiply the list of possible records together to get the answer.
# 7. Print the answer.

# Input:
# Time:      7  15   30
# Distance:  9  40  200

import sys

# Open the input and turn it into lines.
with open(sys.argv[1], 'r') as file:
    races = [line.strip() for line in file]


def main():
    # Create tuples from input
    for race in races:
        # Split the input into a list of tuples
        split
        print(race)


if __name__ == '__main__':
    main()