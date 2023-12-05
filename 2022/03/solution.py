def solution_one(input):
    return __calculate_priorities_sum(input)

def solution_two(input):
    return __calculate_priorities_sum_three_compartments(input)

def __calculate_priorities_sum(input):
    priority_sum = 0
    for line in input:
        compartment_size = int(len(line) / 2)
        first_compartment = set(line[0 : compartment_size])
        second_compartment = set(line[compartment_size : len(line)])

        intersection_list = first_compartment & second_compartment
        for c in intersection_list:
            priority_sum += __calculatePriority(c)

    return priority_sum

def __calculate_priorities_sum_three_compartments(input):
    priority_sum = 0
    for i in range(0, len(input) - 1, 3):
        first_compartment = set(input[i])
        second_compartment = set(input[i + 1])
        third_compartment = set(input[i + 2])

        intersection_list = first_compartment & second_compartment & third_compartment
        for c in intersection_list:
            priority_sum += __calculatePriority(c)
    return priority_sum

# returns priority value for a given character. uses ascii codes to calculate priority
def __calculatePriority(character):
    ascii = ord(character)
    if str(character).isupper():
        priority = ascii - 38
    else:
        priority = ascii - 96
    return priority