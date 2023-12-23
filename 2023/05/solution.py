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

MAPS = [SEED_TO_SOIL_START,
    SOIL_TO_FERTILIZER_START,
    FERTILIZER_TO_WATER_START,
    WATER_TO_LIGHT_START,
    LIGHT_TO_TEMPERATURE_START,
    TEMPERATURE_TO_HUMIDITY_START,
    HUMIDITY_TO_LOCATION_START]

def solution_one(input):
    min_location = sys.maxsize
    seeds = input[0].split(":")[1].strip().split(" ")
    
    for seed in seeds:
        seed = int(seed)
        for map in MAPS:
            seed = __apply_map(seed, map, input)
        # after applying all maps, we end up with location, so find the min
        if seed < min_location:
            min_location = seed
    return min_location

def __apply_map(seed, map_line_start, input):
    for i in range(map_line_start, len(input)):
        line = input[i]
        split = line.split(" ")
        if not line or not split[0].isnumeric():
                break
        
        dest_start = int(split[0])
        source_start = int(split[1])
        range_length = int(split[2])
        source_range = range(source_start, source_start+range_length)
        if seed in source_range:
            # apply transform via mapping
            old = seed
            transform = seed - source_start
            seed = dest_start + transform
            #print(str(old) + "\t->\t" + str(seed))
            # only transform the seed ONCE per mapping
            break
    return seed

def solution_two(input):
    return 0