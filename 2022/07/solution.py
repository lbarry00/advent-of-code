def solution_one(input):
    root = __build_file_system(input)
    __calculate_size(root)
    return __get_sum_sizes_less_than_10k(root)

def solution_two(input):
    return 0

def __build_file_system(input):
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

def __calculate_size(f):
    if isinstance(f, File):
        return f.size
    else:
        for child in f.contents:
            f.size = __calculate_size_r(child)

def __calculate_size_r(f):
    if isinstance(f, File):
        return f.size
    else:
        size = 0
        for child in f.contents:
            f.size += __calculate_size_r(child)
        return size

def __get_sum_sizes_less_than_10k(folder):
    sum = 0
    if folder.size <= 100000:
        sum += folder.size

    for f in folder.contents:
        if isinstance(f, Folder):
            sum += __get_sum_sizes_less_than_10k(f)
    return sum

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