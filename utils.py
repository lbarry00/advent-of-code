def run_solution(solution_function, day):
    path_format = "/Users/leo/code/advent-of-code22/{}/input.txt"
    input_path = path_format.format(day)

    input = read_input(input_path)
    result = solution_function(input)

    print(day + " solution: \t" + str(result))

def read_input(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines