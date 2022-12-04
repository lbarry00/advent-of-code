import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

DAY = "02"

def main():
    utils.run_solution(calculate_part_one, DAY)
    utils.run_solution(calculate_part_two, DAY)


# A -   rock        -   X  
# B -   paper       -   Y
# C -   scissors    -   Z
# paper > rock > scissors 
#   ^---------------v

def calculate_part_one(input):
    total_score = 0

    # winning combinations for you
    victory_map = {
        "X": "C",
        "Y": "A",
        "Z": "B"
    }
    draw_map = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }
    scores_map = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    for line in input:
        opponents_choice = line[0]
        your_choice = line[2]
        round_score = scores_map[your_choice]

        if victory_map[your_choice] == opponents_choice:
            round_score += 6
        elif draw_map[your_choice] == opponents_choice:
            round_score += 3
        # no need to handle loss as it's +0
        total_score += round_score

    return total_score

def calculate_part_two(input):
    total_score = 0

    # what to play based on what opponent plays 
    victory_map = {
        "A": "B",
        "B": "C",
        "C": "A"
    }
    loss_map = {v: k for k, v in victory_map.items()}
    scores_map = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    for line in input:
        opponents_choice = line[0]
        round_result = line[2]
        round_score = 0
        if round_result == "X": 
            your_choice = loss_map[opponents_choice]
        elif round_result == "Y":
            your_choice = opponents_choice
            round_score += 3
        else:
            your_choice = victory_map[opponents_choice]
            round_score += 6
        round_score += scores_map[your_choice]
        total_score += round_score

    return total_score

if __name__ == "__main__":
    main()