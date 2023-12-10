def solution_one(input):
    result = 0
    for line in input:
        idxs = [i for i in range(0, len(line)) if line[i].isdigit()]
        if len(idxs) == 1:
            num = int(line[idxs[0]])
            result += (num * 10) + num
        else:
            first = int(line[idxs[0]])
            last = int(line[idxs[-1]])
            add = (first * 10) + last
            result += add

    return result

def solution_two(input):
    new_input = __convert_words_to_digits(input)

    return solution_one(new_input)

def __convert_words_to_digits(input):
    new_input = []

    # TODO xtwone3four -> "24" 

    for line in input:
        new_line = line.replace("one", "o1ne")
        new_line = new_line.replace("two", "t2wo")
        new_line = new_line.replace("three", "t3hree")
        new_line = new_line.replace("four", "f4our")
        new_line = new_line.replace("five", "f5ive")
        new_line = new_line.replace("six", "s6ix")
        new_line = new_line.replace("seven", "s7even")
        new_line = new_line.replace("eight", "e8ight")
        new_line = new_line.replace("nine", "n9ine")
        new_input.append(new_line)
    
    return new_input