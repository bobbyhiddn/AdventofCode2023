import sys

def main():
    # Open Puzzle Input
    with open(sys.argv[1], 'r') as file:
        grid = [line.strip() for line in file]

    # Define the order of the maps
    map_order = [
        "seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map",
        "water-to-light map", "light-to-temperature map", 
        "temperature-to-humidity map", "humidity-to-location map"
    ]

    # Process the maps and build a dictionary
    map_values = process_maps(grid, map_order)

    # Initialize variable to keep track of the smallest transformed value
    smallest_transformed_value = float('inf')

    # Extract and process each seed range
    for start, length in extract_seed_ranges(grid):
        for seed in range(start, start + length):
            transformed_value = transform_value(seed, map_values, map_order)
            if transformed_value < smallest_transformed_value:
                smallest_transformed_value = transformed_value
    
def extract_seed_ranges(grid):
    for line in grid:
        if line.startswith("seeds:"):
            ranges = [int(x) for x in line.split(":")[1].strip().split()]
            return [(ranges[i], ranges[i+1]) for i in range(0, len(ranges), 2)]
    return []

def process_maps(arg, map_order):
    map_values = {map_name: [] for map_name in map_order}
    current_map = None

    for line in arg:
        line = line.strip()
        if line.endswith(":"):
            current_map = line[:-1]
        elif current_map in map_values:
            values = [int(x) for x in line.split()]
            map_values[current_map].append(values)

    return map_values

def transform_range_bound(value, map_values, map_order):
    for map_name in map_order:
        value = apply_transformation(value, map_values[map_name])
    return value

def transform_value(value, map_values, map_order):
    for map_name in map_order:
        value = apply_transformation(value, map_values[map_name])
    return value

def apply_transformation(value, value_sets):
    transformed = value
    for value_set in value_sets:
        if len(value_set) == 3:
            dest_start, src_start, length = value_set
            if src_start <= value < src_start + length:
                transformed = dest_start + (value - src_start)
                break
    return transformed

if __name__ == "__main__":
    main()
