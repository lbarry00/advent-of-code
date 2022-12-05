import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

DAY = "04"

def main():
    utils.run_solution(get_num_contained_pairs, DAY)
    utils.run_solution(get_overlapping_pairs, DAY)

def get_num_contained_pairs(input):
    contained_pairs_count = 0
    for line in input:
        line_split = line.split(",")
        first_pair = get_tuple_from_string(line_split[0])
        second_pair = get_tuple_from_string(line_split[1])

        if second_pair[0] >= first_pair[0] and second_pair[1] <= first_pair[1]:
            contained_pairs_count += 1
        elif first_pair[0] >= second_pair[0] and first_pair[1] <= second_pair[1]:
            contained_pairs_count += 1

    return contained_pairs_count

def get_overlapping_pairs(input):
    overlapping_pairs = 0
    for line in input:
        line_split = line.split(",")
        first_pair = get_tuple_from_string(line_split[0])
        second_pair = get_tuple_from_string(line_split[1])

        first_range = set(range(first_pair[0], first_pair[1] + 1))
        second_range = set(range(second_pair[0], second_pair[1] + 1))

        if first_range.intersection(second_range):
            overlapping_pairs += 1

    return overlapping_pairs

# param: tuple_string in format of "number-number"
# returns: tuple of (number, number)
def get_tuple_from_string(tuple_string):
    split = tuple_string.split("-")
    return (int(split[0]), int(split[1]))

if __name__ == "__main__":
    main()