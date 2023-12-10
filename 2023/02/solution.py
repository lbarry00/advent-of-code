import re

def solution_one(input):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    sum_possible_games = 0

    for game_line in input:
        game_is_possible = True

        split = game_line.split(":")
        game_id = int(split[0].split(" ")[1])

        rounds = split[1].strip().split(";")
        for round in rounds:
            red = 0
            green = 0
            blue = 0
            for pair in round.split(","):
                pair = pair.split(" ")
                pair = [x for x in pair if x.strip()]
                num = int(pair[0])
                color = pair[1]

                if color == "red":
                    red += num
                elif color == "green":
                    green += num
                elif color == "blue":
                    blue += num
                
                if red > MAX_RED or green > MAX_GREEN or blue > MAX_BLUE:
                    game_is_possible = False
                    break

        if game_is_possible: sum_possible_games += game_id

    return sum_possible_games

def solution_two(input):
    sum_powers = 0

    for game_line in input:
        split = game_line.split(":")
        rounds = split[1].strip().split(";")

        max_red = 0
        max_green = 0
        max_blue = 0
        for round in rounds:
            for pair in round.split(","):
                pair = pair.split(" ")
                pair = [x for x in pair if x.strip()]
                num = int(pair[0])
                color = pair[1]

                if color == "red" and num > max_red:
                    max_red = num
                elif color == "green" and num > max_green:
                    max_green = num
                elif color == "blue" and num > max_blue:
                    max_blue = num
        power = max_red * max_green * max_blue
        sum_powers += power

    return sum_powers