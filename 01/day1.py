import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

DAY = "01"

def main():
    utils.run_solution(calculate_most_calories_carried, DAY)
    utils.run_solution(calculate_top_three_calories_carried, DAY)

def calculate_most_calories_carried(input):
    most_calories_carried = 0
    current_elf = 0

    for input_line in input:
        if not input_line:
            if current_elf > most_calories_carried:
                most_calories_carried = current_elf
            current_elf = 0
        else:
            current_elf += int(input_line)

    return most_calories_carried

def calculate_top_three_calories_carried(input):
    calorie_sums = []
    current_elf = 0

    for input_line in input:
        if not input_line:
            calorie_sums.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(input_line)

    calorie_sums.sort(reverse=True)
    return calorie_sums[0] + calorie_sums[1] + calorie_sums[2]

if __name__ == "__main__":
    main()