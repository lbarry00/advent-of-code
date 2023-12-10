# generates a day folder, empty input.txt, and solution.py files
# EX:
# 2023
# - 01
# - - input.txt
# - - solution.py
import os, shutil

YEAR = "2023"
SOLUTION_TEMPLATE_PATH = "solution-template.py"

def main():
    print("YEAR set as:", YEAR)
    day = __get_day_input()

    year_dir_path = "./" + YEAR
    __generate_directory(year_dir_path, "year")

    day_folder_name = str(day) if day > 9 else "0" + str(day)
    day_folder_path = year_dir_path + "/" + day_folder_name
    __generate_directory(day_folder_path, "day")

    # create empty input.txt file
    input_path = day_folder_path + "/input.txt"
    __generate_file(input_path, "input")

    solution_path = day_folder_path + "/solution.py"
    __copy_solution_template(solution_path)

    print("Done!")

def __get_day_input():
    have_valid_day = False

    while(True):
        day_input = input("Enter DAY:  ")

        if day_input.isnumeric():
            day = int(day_input)
            if day >= 1 and day <= 31:
                return day
            else:
                print("ERROR: Enter a valid day (1-31) in December.\n")
        else:
            print("ERROR: Enter a number.\n")

def __generate_directory(path, folder_friendly_name):
    if not os.path.exists(path):
        print("Creating " + folder_friendly_name + " directory.")
        os.mkdir(path)
    else: print(folder_friendly_name + " directory already exists. Skipping...")

def __generate_file(path, file_friendly_name):
    if not os.path.isfile(path):
        print("Creating " + file_friendly_name + " file.")
        input_file = open(path, "w")
        input_file.close()
    else: print(file_friendly_name + " file already exists. Skipping...")

def __copy_solution_template(destination_path):
    if not os.path.isfile(SOLUTION_TEMPLATE_PATH):
        print("Solution template file is missing! Check that it exists at: " + SOLUTION_TEMPLATE_PATH)
    elif os.path.isfile(destination_path):
        print("Solution file already exists in day directory. Skipping...")
    else:
        print("Copying solution template file to day directory.")
        shutil.copyfile(SOLUTION_TEMPLATE_PATH, destination_path)
    
if __name__ == "__main__":
    main()