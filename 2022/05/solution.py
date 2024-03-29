from collections import deque
import itertools

def solution_one(input):
    return __get_top_stack_items_after_rearrange(input)

def solution_two(input):
    return __get_top_stack_items_after_rearrange_moving_inorder(input)

def __get_top_stack_items_after_rearrange(input):
    stacks_dict = __get_stacks_dict_from_raw_input(input[0:8])
    operations = __get_stack_operations_from_raw_input(input[10:len(input)])

    for op in operations:
        crates_moved = 0
        while crates_moved < op.crates_to_move:
            item_to_move = stacks_dict[op.source_stack].pop()
            stacks_dict[op.target_stack].append(item_to_move)
            crates_moved += 1

    return __get_result_string_from_stacks(stacks_dict)

def __get_top_stack_items_after_rearrange_moving_inorder(input):
    stacks_dict = __get_stacks_dict_from_raw_input(input[0:8])
    operations = __get_stack_operations_from_raw_input(input[10:len(input)])

    for op in operations:
        crates_moved = 0
        items_to_move = []
        for i in range(op.crates_to_move):
            source = stacks_dict[op.source_stack]
            items_to_move += source.pop()
        
        for i in reversed(items_to_move):
            stacks_dict[op.target_stack].append(i)

    return __get_result_string_from_stacks(stacks_dict)

# returns dict {index: deque()}
def __get_stacks_dict_from_raw_input(input_lines):
    result = {}
    for i in range(9):
        result[i] = deque()
    
    for line in input_lines:
        # for keeping track of which stack we're adding to 
        stack_iterator = 0
        # iterate by +4 to skip whitespace/brackets
        for i in range(1, len(line) - 1, 4):
            value = line[i]
            if value != " ":
                result[stack_iterator].appendleft(value)
            stack_iterator += 1

    return result

def __get_stack_operations_from_raw_input(input_lines):
    result = []
    for line in input_lines:
        words = line.split(" ")
        new_stack = StackOperation(words[1], words[3], words[5])
        result.append(new_stack)
    return result

def __get_result_string_from_stacks(stacks_dict):
    result_str = ""
    for i in stacks_dict.keys():
        top_item = stacks_dict[i].pop()
        result_str += top_item
    return result_str

class StackOperation:
    def __init__(self, crates, source, target):
        self.crates_to_move = int(crates)
        self.source_stack = int(source) - 1
        self.target_stack = int(target) - 1