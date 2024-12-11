"""
Advent of Code {year} - Day {day}
"""
import pytest
import time
from aocd import submit
from aocd.models import Puzzle

def part1(input_data):
    print(input_data)
    # TODO: Implement Part 1 solution
    pass

def part2(input_data):
    # TODO: Implement Part 2 solution
    pass

if __name__ == "__main__":

    start_time = time.perf_counter()

    year = {year}
    day = {day}
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 0
    expect_2 = 0
    start_time_part_1 = time.perf_counter()

    answer1 = part1(input_data)
    end_time_part_1 = time.perf_counter()
    duration_part_1 = end_time_part_1 - start_time_part_1
    print(f"Part_1 executed in {duration_part_1:.6f} seconds.")
    if answer1 is not None:
        print(f"Part 1 Answer: {{answer1}}")
        assert answer1 == expect_1

        # submit(answer1, part='a', year=year, day=day)

    start_time_part_2 = time.perf_counter()
    answer2 = part2(input_data)
    end_time_part_2 = time.perf_counter()
    duration_part_2 = end_time_part_2 - start_time_part_2
    print(f"Part_2 executed in {duration_part_2:.6f} seconds.")

    if answer2 is not None:
        print(f"Part 2 Answer: {{answer2}}")
        assert answer2 == expect_2

        # submit(answer2, part='b', year=year, day=day)

    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Script executed in {duration:.6f} seconds.")
