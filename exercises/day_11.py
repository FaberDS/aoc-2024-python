"""
Advent of Code 2024 - Day 11
"""

import utils.parser
import utils.number
from collections import defaultdict
import time
from aocd import submit
from aocd.models import Puzzle

split_history = {}

def split_number(num,length):
    if num in split_history:
        return split_history[num]
    length = utils.number.digit_count(num)
    mid = length // 2
    divisor = 10 ** (length - mid)
    left = num // divisor
    right = num % divisor
    split_history[num] = (left, right)
    return left, right

def arrange_stones_dict(stones_dict):
    new_stones_dict = defaultdict(int)
    for key,value in stones_dict.items():
        d_count = utils.number.digit_count(key)
        match key:
            case 0: new_stones_dict[1] += value
            case val if  d_count % 2 == 0:

                left, right = split_number(val,d_count)
                new_stones_dict[left] += value
                new_stones_dict[right] += value
            case _:
                new_key = 2024 * key
                new_stones_dict[new_key] += value
    return new_stones_dict

def solve(stones,iterations):
    stones_dict = defaultdict(int)
    for stone in stones:
        if stone in stones_dict:
            stones_dict[stone] += 1
        else:
            stones_dict[stone] = 1
    for i in range(iterations):
        stones_dict = arrange_stones_dict(stones_dict)
    return sum(stones_dict.values())

if __name__ == "__main__":

    start_time = time.perf_counter()

    year = 2024
    day = 11
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data

    expect_1 = 216996
    expect_2 = 257335372288947
    # Solve Part 1

    stones = utils.parser.split_numbers(input_data, " ")

    start_time_part_1 = time.perf_counter()

    answer1 = solve(stones,25)
    end_time_part_1 = time.perf_counter()
    duration_part_1 = end_time_part_1 - start_time_part_1
    print(f"Part_1 executed in {duration_part_1:.6f} seconds.")
    if answer1 is not None:
        print(f"Part 1 Answer: {answer1}")
        # assert answer1 == expect_1

        # Uncomment the following line to submit Part 1 answer
        # submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    start_time_part_2 = time.perf_counter()
    answer2 = solve(stones,75)
    end_time_part_2 = time.perf_counter()
    duration_part_2 = end_time_part_2 - start_time_part_2
    print(f"Part_2 executed in {duration_part_2:.6f} seconds.")

    start_time_part_3 = time.perf_counter()
    answer3 = solve(stones, 1000)
    print(f"Part_3 1000 iterations = {answer3}")

    end_time_part_3 = time.perf_counter()
    duration_part_3 = end_time_part_3 - start_time_part_3
    print(f"Part_3 executed in {duration_part_3:.6f} seconds.")
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        # assert answer2 == expect_2

        # Uncomment the following line to submit Part 2 answer
        # submit(answer2, part='b', year=year, day=day)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Script executed in {duration:.6f} seconds.")
