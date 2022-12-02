import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

DAY = "01"

def main():
    utils.run_solution(solution_one, DAY)
    utils.run_solution(solution_two, DAY)

def solution_one(input):
    return 0

def solution_two(input):
    return 0

if __name__ == "__main__":
    main()