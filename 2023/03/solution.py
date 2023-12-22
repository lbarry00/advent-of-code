import re

# remove all numbers and "." from a string (to find the special chars)
find_symbols_pattern = r"\d+|[.]"

def solution_one(input):
    sum = 0
    for y in range(0, len(input)):
        line = input[y]
        line_iter = iter(range(0, len(line)))

        latest_visited = 0
        for x in line_iter:
            c = line[x]
            symbol_match = re.sub(find_symbols_pattern, "", c)
            if symbol_match:
                part_nums = __get_part_nums_list(x, y, line, input)

                for part_num in part_nums:
                    sum += part_num
    return sum

def solution_two(input):
    sum_gear_ratios = 0

    for y in range(0, len(input)):
        line = input[y]
        line_iter = iter(range(0, len(line)))

        latest_visited = 0
        for x in line_iter:
            c = line[x]
            if c == "*":
                part_nums = __get_part_nums_list(x, y,line, input)

                if len(part_nums) == 2:
                    gear_ratio = part_nums[0] * part_nums[1]
                    sum_gear_ratios += gear_ratio

    return sum_gear_ratios

def __get_part_nums_list(x, y, line, input):
    part_nums = []
    
    # left, right, up, down
    part_nums.extend(__find_nums(x - 1, line, part_nums))
    part_nums.extend(__find_nums(x + 1, line, part_nums))
    part_nums.extend(__find_nums(x, input[y - 1], part_nums))
    part_nums.extend(__find_nums(x, input[y + 1], part_nums))

    # diagonals: topleft, topright, bottomleft, bottomright
    part_nums.extend(__find_nums(x - 1, input[y - 1], part_nums))
    part_nums.extend(__find_nums(x + 1, input[y - 1], part_nums))
    part_nums.extend(__find_nums(x - 1, input[y + 1], part_nums))
    part_nums.extend(__find_nums(x + 1, input[y + 1], part_nums))

    return part_nums

def __find_nums(x, line, part_nums):
    distinct_nums = []
    num = ""
    original_x = x
    if line[x].isnumeric():
        while line[x].isnumeric():
            num = num + line[x]
            x += 1
        x = original_x - 1
        while line[x].isnumeric():
            num = line[x] + num
            x -= 1

    if num:
        num = int(num)
        if num != 0 and num not in part_nums:
            distinct_nums.append(num)

    return distinct_nums