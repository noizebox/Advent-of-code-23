from data import DAY_3 as DATA


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


def create_symbol_map(data):
    map = [ [0]*len(data) for i in range(len(data))]
    for line, row in zip(data, range(0, len(data))):
        for ch, col in zip(line, range(0, len(data))):
            if not ch.isnumeric() and ch != '.':
                print (ch)
                l = len(data) - 1
                map[min(row + 1, l)][min(col + 1, l)] = 1
                map[min(row + 1, l)][col] = 1
                map[min(row + 1, l)][max(col - 1, 0)] = 1
                map[row][max(col - 1, 0)] = 1
                map[max(row -1, 0)][max(col - 1, 0)] = 1
                map[max(row -1, 0)][col] = 1
                map[max(row -1, 0)][min(col + 1, l)] = 1
                map[row][min(col + 1, l)] = 1

    return map

def is_valid(coord, map):
    return map[coord[0]][coord[1]] == 1

def solve_part_1(data):
    map = create_symbol_map(data)
    for line in map:
        print(line)

    v_sum = 0
    current_no = ""
    valid = False

    for line, row in zip(data, range(0, len(data))):
        for ch, col in zip(line, range(0, len(data))):
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



def main():
    print(f'Part 1: {solve_part_1(DATA)}')
    #print(f'Part 2: {solve_part_2(DATA)}')

if __name__ == "__main__": main()