from data import DAY_2 as DATA

COLOURS = ['red', 'green', 'blue']
MAX_COLOURS = {'red':12, 'green':13, 'blue':14}

def pre_parse_data(data):
    parsed = {}
    for line in data:
        id, sep, games = line.partition(':')
        game_id = int(id.split(' ')[1])
        parsed[game_id] = []
        for sub_game in games.split(';'):
            g = {col : 0 for col in COLOURS}
            for col in COLOURS:
                before,sep,after = sub_game.partition(col)
                if len(sep) > 0:
                    g[col] = int(before.strip(' ').split(' ')[-1])
            parsed[game_id].append(g)

    return parsed

def game_possible(game):
    for colour, max_val  in MAX_COLOURS.items():
        if game[colour] > max_val:
            return False
    return True

def games_possible(games):
    for game in games:
        if not game_possible(game):
            return False
    return True

def min_power(games):
    c = {col : 0 for col in COLOURS}
    for game in games:
        for col in c.keys():
            c[col] = max(game[col], c[col])
    return c['red'] * c['blue'] * c['green']


def solve_part_1(data):
    p = pre_parse_data(data)
    return sum([id for id, games in p.items() if games_possible(games)])

def solve_part_2(data):
    p = pre_parse_data(data)
    return sum([min_power(games) for games in p.values()])

def main():
    print(f'Part 1: {solve_part_1(DATA)}')
    print(f'Part 2: {solve_part_2(DATA)}')

if __name__ == "__main__": main()