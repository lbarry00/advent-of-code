import re

card_number_pattern = r"\d+(?=:)"

def solution_one(input):
    total = 0
    for line in input:
        substr = line.split(":")[1].split("|")
        winning_nums = set(filter(None, substr[0].split(" ")))
        your_nums = list(filter(None, substr[1].split(" ")))

        card_total = 0
        for n in your_nums:
            if n in winning_nums:
                if card_total == 0:
                    card_total += 1
                else:
                    card_total *= 2
        total += card_total
        
    return total

# this is so slow lol
def solution_two(input):
    cards = {}
    total = 0

    i = 0
    while i < len(input):
        line = input[i]
        
        card_num = get_card_number(line)
        matching_nums = get_matching_nums(line)
        if card_num in cards:
            cards[card_num] += 1
            for j in range(cards[card_num]):
                cards = process_card(input, line, cards)
        else:
            cards[card_num] = 1
            cards = process_card(input, line, cards)

        i += 1

    for k in cards.keys():
        total += cards[k]

    return total

def process_card(input, line, cards):
    card_num = get_card_number(line)
    matching_nums = get_matching_nums(line)

    for j in range(card_num, card_num+matching_nums):
        c = get_card_number(input[j])
        if c in cards:
            cards[c] += 1
        else:
            cards[c] = 1
    
    return cards

def get_matching_nums(line):
    substr = line.split(":")[1].split("|")
    winning_nums = set(filter(None, substr[0].split(" ")))
    your_nums = list(filter(None, substr[1].split(" ")))

    matching_nums = 0
    for n in your_nums:
        if n in winning_nums:
            matching_nums += 1
    
    return matching_nums

def get_card_number(line):
    return int(re.search(card_number_pattern, line).group(0))