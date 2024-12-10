"""
Advent of Code 2024 - Day 9
"""
import pytest
def next_file_nr(nr):
    nr += 1
    if nr > 9:
        nr = 0
    return nr
def print_separator():
    print(
        f"\n"
        f"------------------------------------------------------------\n",
        f"\n"
    )

def part1(input_data):

    print_separator()
    # input_data = '2333133121414131402'
    input = list(map(int, list(input_data)))

    memory = []
    file_nr = 0
    for i,p in enumerate(input):
        if i % 2 == 0:
            memory.extend([file_nr] * p)
            file_nr += 1
        else:
            memory.extend([None] * p)

    p_free = 0
    p_file = len(memory) - 1
    while True:
         # push p_free forwards
        while p_free < p_file and memory[p_free] is not None:
            p_free += 1
        # pull p_file back
        while p_free < p_file and memory[p_file] is None:
            p_file -= 1
        if p_free >= p_file:
            break
        memory[p_free], memory[p_file] = memory[p_file], memory[p_free]
    return calc_checksum(memory)

def calc_checksum(memory):
    checksum = 0
    for i, id_num in enumerate(memory):
        if id_num is not None:
            checksum += i * id_num

    return checksum
def part2(input_data):
    input = list(map(int, list(input_data)))
    memory = []
    file_nr = 0
    for i, p in enumerate(input):
        if i % 2 == 0:
            memory.extend([file_nr] * p)
            file_nr += 1
        else:
            memory.extend([None] * p)
    p_file = len(memory) - 1
    id_num = max(x for x in memory if x is not None)
    while id_num >= 0:
        # pull p_file back
        while 0 < p_file and memory[p_file] != id_num:
            p_file -= 1
        if p_file == 0:
            break
        # find size of file
        p_temp = p_file
        while memory[p_temp] == id_num:
            p_temp -= 1
        file_size = p_file - p_temp
        # find first free block to fit file
        for p_free in range(0, p_file - file_size + 1):
            if all(memory[p_free + k] is None for k in range(file_size)):
                # move file
                for k in range(file_size):
                    memory[p_free + k], memory[p_file - k] = memory[p_file - k], memory[p_free + k]
                break
        p_file -= file_size
        id_num -= 1
    return calc_checksum(memory)

if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 9
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 6259790630969
    # expect_1 = 1928
    expect_2 = 6289564433984
    # Solve Part 1
    answer1 = part1(input_data)
    if answer1 is not None:
        print(f"Part 1 Answer: {answer1}")
        assert answer1 == expect_1

        # Uncomment the following line to submit Part 1 answer
        # submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        assert answer2 == expect_2

        # Uncomment the following line to submit Part 2 answer
        # submit(answer2, part='b', year=year, day=day)
