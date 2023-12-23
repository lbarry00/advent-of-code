import sys

# example line starts
#SEED_TO_SOIL_START = 3
#SOIL_TO_FERTILIZER_START = 7
#FERTILIZER_TO_WATER_START = 12
#WATER_TO_LIGHT_START = 18
#LIGHT_TO_TEMPERATURE_START = 22
#TEMPERATURE_TO_HUMIDITY_START = 27
#HUMIDITY_TO_LOCATION_START = 31

SEED_TO_SOIL_START = 3
SOIL_TO_FERTILIZER_START = 49
FERTILIZER_TO_WATER_START = 73
WATER_TO_LIGHT_START = 115
LIGHT_TO_TEMPERATURE_START = 160
TEMPERATURE_TO_HUMIDITY_START = 196
HUMIDITY_TO_LOCATION_START = 243

def solution_one(input):
    min_location = sys.maxsize
    seeds = input[0].split(":")[1].strip().split(" ")

    mappings_list = []
    mappings_list.append(__build_map(SEED_TO_SOIL_START, input))
    mappings_list.append(__build_map(SOIL_TO_FERTILIZER_START, input))
    mappings_list.append(__build_map(FERTILIZER_TO_WATER_START, input))
    mappings_list.append(__build_map(WATER_TO_LIGHT_START, input))
    mappings_list.append(__build_map(LIGHT_TO_TEMPERATURE_START, input))
    mappings_list.append(__build_map(TEMPERATURE_TO_HUMIDITY_START, input))
    mappings_list.append(__build_map(HUMIDITY_TO_LOCATION_START, input))

    # apply each map
    items = seeds
    for map in mappings_list:
        for i in range(0, len(items)):
            seed = int(items[i])
            if seed in map:
                items[i] = map[seed]
            else: pass

    # look for smallest location value
    for loc in items:
        if int(loc) < min_location:
            min_location = int(loc)

    return min_location

def __build_map(map_line_start, input):
    map = {}
    for i in range(map_line_start, len(input)):
        line = input[i]
        if not line: break
        nums = line.split(" ")
        dest_start = nums[0]
        source_start = nums[1]
        range_length = nums[2]
        for j in range(0, int(range_length)):
            map[int(source_start) + j] = int(dest_start) + j
    return map

def solution_two(input):
    return 0