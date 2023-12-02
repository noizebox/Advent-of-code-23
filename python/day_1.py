from data import DAY_1 as DATA

CHARMAP = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def parse_line(line):
    digits = [int(d) for d in line if d.isdigit()]
    return digits[0] * 10 + digits[-1]

def replace_line(line):
    for digit_str, digit in CHARMAP.items():
        # As words are allowed to overlap (twone should parse as 21), put the digit in the middle of the word
        line = line.replace(digit_str, f'{digit_str[0]}{digit}{digit_str[1:]}')
    return line

def solve_part_1(data):
    return sum([parse_line(line) for line in data])

def solve_part_2(data):
    return sum([parse_line(replace_line(line)) for line in data])

def main():
    print(f'Part 1: {solve_part_1(DATA)}')
    print(f'Part 2: {solve_part_2(DATA)}')

if __name__ == "__main__": main()