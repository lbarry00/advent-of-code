import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

DAY = "06"

def main():
    utils.run_solution(find_first_four_distinct, DAY)
    utils.run_solution(find_first_fourteen_distinct, DAY)

def find_first_four_distinct(input):
    # due to driver code, input comes as an array,
    # but this input only has 1 line so make it a regular string
    input = input[0]
    for i in range(0, len(input)):
        substring_set = set(input[i:i+4])
        if len(substring_set) == 4:
            return i + 4
    return -1

def find_first_fourteen_distinct(input):
    input = input[0]
    for i in range(0, len(input)):
        substring_set = set(input[i:i+14])
        if len(substring_set) == 14:
            return i + 14
    return -1

def find_first_n_distinct(input, substring_size):
    input = input[0]
    for i in range(0, len(input)):
        substring_set = set(input[i:i+substring_size])
        if len(substring_set) == substring_size:
            return i + substring_size
    return -1

def solution_two(input):
    return 0

if __name__ == "__main__":
    main()