import os, sys, importlib

DAY = "08"
YEAR = "2022"

def main():
    __run_full_solution(YEAR, DAY)

def __run_full_solution(year, day):
    day_directory_format = "/Users/leo/code/advent-of-code/{}/{}/"
    day_directory = day_directory_format.format(year, day)

    sys.path.append(day_directory)

    solution = importlib.import_module("solution")

    input_path = day_directory + "input.txt"
    input = __read_input(input_path)
    
    print("Day " + day + " Solutions:")
    print("\tPart 1:")
    __run_and_print_solution(solution.solution_one, input, day)
    print("\tPart 2")
    __run_and_print_solution(solution.solution_two, input, day)

def __run_and_print_solution(solution_func, input, day):
    result = solution_func(input)
    print("\t\t" + str(result))

def __read_input(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines

if __name__ == "__main__":
    main()