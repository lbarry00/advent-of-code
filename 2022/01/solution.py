def solution_one(input):
    return __calculate_most_calories_carried(input)

def solution_two(input):
    return __calculate_top_three_calories_carried(input)

def __calculate_most_calories_carried(input):
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

def __calculate_top_three_calories_carried(input):
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