import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

DAY = "07"

def main():
    utils.run_solution(solution_one, DAY)
    utils.run_solution(solution_two, DAY)

def solution_one(input):
    root = build_file_system(input)
    calculate_size(root)
    return get_sum_sizes_less_than_10k(root)

def build_file_system(input):
    root = Folder("/")
    root.parent = None
    cwd = root
    for line in input:
        line_split = line.split(" ")
        if line_split[0] == "$":
            if line_split[1] == "cd":
                args = line_split[2]
                if args == ".." and cwd.parent != None:
                    cwd = cwd.parent
                elif args == "/":
                    cwd = root
                else: # cd-ing to a child directory
                    cd_target = cwd.try_get_child_folder(args)
                    cwd = cd_target
        elif line_split[0] == "dir":
            new_folder = Folder(line_split[1])
            new_folder.parent = cwd
            cwd.append_contents(new_folder)
        elif int(line_split[0]):
            new_file = File(int(line_split[0]), line_split[1])
            cwd.append_contents(new_file)
    return root

def calculate_size(f):
    if isinstance(f, File):
        return f.size
    else:
        for child in f.contents:
            f.size = calculate_size_r(child)

def calculate_size_r(f):
    if isinstance(f, File):
        return f.size
    else:
        size = 0
        for child in f.contents:
            f.size += calculate_size_r(child)
        return size

def get_sum_sizes_less_than_10k(folder):
    sum = 0
    if folder.size <= 100000:
        sum += folder.size

    for f in folder.contents:
        if isinstance(f, Folder):
            sum += get_sum_sizes_less_than_10k(f)
    return sum

def solution_two(input):
    return 0

class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

class Folder:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.contents = []
        self.parent = None

    def set_contents(self, new_contents):
        self.contents = new_contents
    def append_contents(self, new_contents):
        self.contents.append(new_contents)
    def try_get_child_folder(self, folder_name):
        for f in self.contents:
            if f.name == folder_name:
                return f
        return None

if __name__ == "__main__":
    main()