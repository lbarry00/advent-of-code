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
            # hack because I can't be bothered to figure out how
            # to skip multiple iterations (num_digits) in python
            if x < latest_visited: continue

            c = line[x]
            if c.isnumeric():
                num = int(c)
                num_digits = 1
                # get the full number
                for k in range(x + 1, len(line)):
                    d = line[k]
                    if d.isnumeric():
                        num *= 10
                        num += int(d)
                        num_digits += 1
                    else: break
                
                latest_visited = x + num_digits
                
                # note: I cheated and added a perimeter of dots around the original input so
                # there's no need to worry about hitting an out of bounds
                above = input[y-1][x-1:x+num_digits+1]
                above = re.sub(find_symbols_pattern, "", above)

                below = input[y+1][x -1:x+num_digits+1]
                below = re.sub(find_symbols_pattern, "", below)

                left = line[x-1]
                left = re.sub(find_symbols_pattern, "", left)

                right = line[x+num_digits]
                right = re.sub(find_symbols_pattern, "", right)

                if above:
                    sum += num
                elif below:
                    sum += num
                elif left:
                    sum += num
                elif right:
                    sum += num

    return sum

def solution_two(input):

    return 0