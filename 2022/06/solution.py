def solution_one(input):
    return __find_first_four_distinct(input)

def solution_two(input):
    return __find_first_fourteen_distinct(input)

def __find_first_four_distinct(input):
    # due to driver code, input comes as an array,
    # but this input only has 1 line so make it a regular string
    input = input[0]
    for i in range(0, len(input)):
        substring_set = set(input[i:i+4])
        if len(substring_set) == 4:
            return i + 4
    return -1

def __find_first_fourteen_distinct(input):
    input = input[0]
    for i in range(0, len(input)):
        substring_set = set(input[i:i+14])
        if len(substring_set) == 14:
            return i + 14
    return -1

def __find_first_n_distinct(input, substring_size):
    input = input[0]
    for i in range(0, len(input)):
        substring_set = set(input[i:i+substring_size])
        if len(substring_set) == substring_size:
            return i + substring_size
    return -1