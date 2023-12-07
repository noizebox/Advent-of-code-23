from data import DAY_4 as DATA

def parse_cards(data):
    cards = []
    for line in data:
        winning = [int(n) for n in line.split('|')[0].split(':')[1].split(' ') if len(n.strip(' ')) > 0]
        own = [int(n) for n in line.split('|')[1].split(' ') if len(n.strip(' ')) > 0]
        cards.append({'winning' : winning, 'own': own})

    return cards

def count_winning_numbers(cards):
    win = []
    for card in cards:
        win.append(len([n for n in card['own'] if n in card['winning']]))
    return win

def solve_part_1(data):
    cards = parse_cards(data)
    win = count_winning_numbers(cards)
    return sum([2 ** (n - 1) for n in win if n > 0])

def solve_part_2(data):
    cards = parse_cards(data)
    win = count_winning_numbers(cards)
    multipliers = [1]*len(win)
    for i, card  in enumerate(win):
        for j in range(i + 1, i + card + 1):
            multipliers[j] += multipliers[i]

    return sum(multipliers)

def main():
    print(f'Part 1: {solve_part_1(DATA)}')
    print(f'Part 2: {solve_part_2(DATA)}')

if __name__ == "__main__": main()