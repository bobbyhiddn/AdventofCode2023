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

def parse_races():
    times = []
    distances = []
    # Assuming the first line in races is for times and the second for distances
    if races:
        times = list(map(int, races[0].replace("Time:", "").strip().split()))
    if len(races) > 1:
        distances = list(map(int, races[1].replace("Distance:", "").strip().split()))

    # Pair each time with its corresponding distance
    return list(zip(times, distances))

def find_records(race_data):
    all_records = []  # This will be a list of lists
    # Process each race
    for race_time, record_distance in race_data:
        race_records = []  # List to hold records for the current race
        distance = 0
        for i in range(race_time):
            distance = i * (race_time - i)
            if distance > record_distance:
                race_records.append(distance)  # Append the record to the current race's list
        all_records.append(race_records)  # Append the current race's records to the overall list
    return all_records


def main():
    # Parse the races and find records
    race_data = parse_races()
    print(race_data)
    records = find_records(race_data)
    print(records)
    answer = 1
    for record in records:
        answer *= len(record)
        
    print("Answer: ", answer)

if __name__ == '__main__':
    main()
