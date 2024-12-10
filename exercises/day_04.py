"""
Advent of Code 2024 - Day 4
"""
import pytest

# count XMAS
# - horizontal
# - backward
# - vertical
# - diagonal
def count_diagonal_tl_br(a,kw):
    n = len(kw)
    count = 0
    rows = len(a)
    cols = len(a[0])

    # Traverse diagonals starting from each row of the first column
    for start_row in range(rows):
        word = ""
        for k in range(min(rows - start_row, cols)):
            word += a[start_row + k][k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    # Traverse diagonals starting from each column of the first row (except the first element)
    for start_col in range(1, cols):
        word = ""
        for k in range(min(rows, cols - start_col)):
            word += a[k][start_col + k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window
    return count

def count_diagonal_all_directions(a, kw):
    n = len(kw)
    count = 0
    rows = len(a)
    cols = len(a[0])

    # Top-left to bottom-right
    for start_row in range(rows):
        word = ""
        for k in range(min(rows - start_row, cols)):
            word += a[start_row + k][k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    for start_col in range(1, cols):
        word = ""
        for k in range(min(rows, cols - start_col)):
            word += a[k][start_col + k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    # Top-right to bottom-left
    for start_row in range(rows):
        word = ""
        for k in range(min(rows - start_row, cols)):
            word += a[start_row + k][cols - 1 - k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    for start_col in range(cols - 2, -1, -1):
        word = ""
        for k in range(min(rows, start_col + 1)):
            word += a[k][start_col - k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    # Bottom-left to top-right
    for start_row in range(rows - 1, -1, -1):
        word = ""
        for k in range(min(start_row + 1, cols)):
            word += a[start_row - k][k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    for start_col in range(1, cols):
        word = ""
        for k in range(min(rows, cols - start_col)):
            word += a[rows - 1 - k][start_col + k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    # Bottom-right to top-left
    for start_row in range(rows - 1, -1, -1):
        word = ""
        for k in range(min(start_row + 1, cols)):
            word += a[start_row - k][cols - 1 - k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    for start_col in range(cols - 2, -1, -1):
        word = ""
        for k in range(min(rows, start_col + 1)):
            word += a[rows - 1 - k][start_col - k]
            if len(word) == n:
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window

    return count

def count_vertical(a,kw):
    n = len(kw)
    count = 0
    cols = len(a[0])  # Number of columns
    rows = len(a)  # Number of rows

    # Iterate column by column
    for col in range(cols):
        word = ""
        for row in range(rows):
            word += a[row][col]  # Collect vertical characters
            if len(word) == n:
                # print(f"{col=} | {row=} | {word=}")
                if word == kw:
                    count += 1
                word = word[1:]  # Slide window to allow overlap
    return count
def count_horinzontal(a,kw):
    n = len(kw)
    count = 0
    for j, row in enumerate(a):

        for i in range(0, len(row)):
            word = row[i:i + n]
            if word == kw:
                count += 1
        reversed_raw = row[::-1]
        for i in range(0, len(reversed_raw)):
            word = reversed_raw[i:i + n]
            if word == kw:
                count += 1
    return count

def calc(grid):
    rows = grid#.split("\n")
    row_count = len(rows)
    col_count = len(rows[0])
    pattern_count = 0

    for r in range(row_count - 2):
        for c in range(col_count - 2):
            top_left = rows[r][c]
            top_right = rows[r][c + 2]
            middle = rows[r + 1][c + 1]
            bottom_left = rows[r + 2][c]
            bottom_right = rows[r + 2][c + 2]

            if (
                middle == 'A' and
                ((top_left == 'M' and bottom_right == 'S') or (top_left == 'S' and bottom_right == 'M')) and
                ((top_right == 'M' and bottom_left == 'S') or (top_right == 'S' and bottom_left == 'M'))
            ):
                pattern_count += 1

    return pattern_count

# # Test Input
# text = (
#     ".M.S......\n"
#     "..A..MSMS.\n"
#     ".M.S.MAA..\n"
#     "..A.ASMSM.\n"
#     ".M.S.M....\n"
#     "..........\n"
#     "S.S.S.S.S.\n"
#     ".A.A.A.A..\n"
#     "M.M.M.M.M



# M.S
# .A.
# M.S
def part1(input_data):
    KW = "XMAS"

    m_1 = input_data.split('\n')
    m_2 = [list(raw) for raw in m_1]

    # for row in m_2[::-1]:
    #     print(row)

    h_count = count_horinzontal(m_1,KW)
    print(f'{h_count=}')


    v_count_down = count_vertical(m_2, KW)
    v_count_up = count_vertical(m_2[::-1], KW)
    # diagonal_tl = count_diagonal_tl_br(m_2, KW)
    diagonal = count_diagonal_all_directions(m_2, KW)
    print(f'{diagonal=}')
    # print(f'vertical: {v_count_down=} { v_count_up=}')
    # diagonal_down_count = 0#count_diagonal(m_2, KW)
    # diagonal_up_count =count_diagonal(m_2[::-1], KW)
    # print(f'{diagonal_down_count=} | {diagonal_up_count=}')
    total_occurance = v_count_down + v_count_up + h_count + diagonal
    return total_occurance

def part2(input_data):
    # print(f"\n{input_data}")
    # m_1 = input_data.split('\n')
    # print(f"\n{len(m_1[0])}")
    input_data =[]
    file_name = "day_4_thomas.txt"
    with open(file_name, 'r') as file:
        for line in file:
            input_data.append(line.strip())
    print(f"\n{input_data=}")

    # m_1 = input_data.split('\n')
    m_1 = input_data
    m_2 = [list(raw) for raw in m_1]
    print(f"{m_2=}")
    count = calc(m_2)

    return count

if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 4
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 0
    expect_2 = 1890
    # Solve Part 1
    #answer1 = part1(input_data)
    # if answer1 is not None:
    #     print(f"Part 1 Answer: {answer1}")
    #     #assert answer1 == expect_1
    #
    #     # Uncomment the following line to submit Part 1 answer
    #     submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        assert answer2 == expect_2

        # Uncomment the following line to submit Part 2 answer
        #submit(answer2, part='b', year=year, day=day)
