from data import DAY_3 as DATA
from collections import defaultdict

TEST_DATA = ['467..114..',
             '...*......',
             '..35..633.',
             '......#...',
             '617*......',
             '.....+.58.',
             '..592.....',
             '......755.',
             '...$.*....',
             '.664.598..']


def create_symbol_map(data, symbol = None):
    map = [ [0]*len(data) for i in range(len(data))]
    gear_id = 1
    for row, line in enumerate(data):
        for col, ch in enumerate(line):
            if not ch.isnumeric() and ch != '.':
                if symbol and ch != symbol:
                    continue
                l = len(data) - 1
                map[min(row + 1, l)][min(col + 1, l)] = gear_id
                map[min(row + 1, l)][col] = gear_id
                map[min(row + 1, l)][max(col - 1, 0)] = gear_id
                map[row][max(col - 1, 0)] = gear_id
                map[max(row -1, 0)][max(col - 1, 0)] = gear_id
                map[max(row -1, 0)][col] = gear_id
                map[max(row -1, 0)][min(col + 1, l)] = gear_id
                map[row][min(col + 1, l)] = gear_id
                gear_id += 1

    return map

def is_valid(coord, map):
    return map[coord[0]][coord[1]] == 1

def solve_part_1(data):
    map = create_symbol_map(data)
    v_sum = 0
    current_no = ""
    valid = False

    for row, line in enumerate(data):
        for col, ch in enumerate(line):
            if ch.isnumeric():
                valid = valid or is_valid([row, col], map)
                current_no += (ch)
            else:
                if len(current_no) > 0 and valid:
                    v_sum += int(current_no)
                current_no = ""
                valid = False

        if len(current_no) > 0 and valid:
            v_sum += int(current_no)
        current_no = ""
        valid = False                

    return v_sum

def solve_part_2(data):
    map = create_symbol_map(data, '*')
    gears = defaultdict(list)
    current_no = ""
    gear_id = 0

    for row, line in enumerate(data):
        for col, ch in enumerate(line):
            if ch.isnumeric():
                current_no += (ch)
                gear_id = max(gear_id, map[row][col])
            else:
                if len(current_no) > 0:
                    gears[gear_id].append(int(current_no))
                current_no = ""
                gear_id = 0

        if len(current_no) > 0:
            gears[gear_id].append(int(current_no))
        current_no = ""
        gear_id = 0

    return sum([gear[0] * gear[1] for id, gear in gears.items() if id > 0 and len(gear) == 2])



def main():
    print(f'Part 1: {solve_part_1(DATA)}')
    print(f'Part 2: {solve_part_2(DATA)}')

if __name__ == "__main__": main()