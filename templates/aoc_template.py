"""
Advent of Code {year} - Day {day}
"""
import pytest

def part1(input_data):
    print(input_data)
    # TODO: Implement Part 1 solution
    pass

def part2(input_data):
    # TODO: Implement Part 2 solution
    pass

if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = {year}
    day = {day}
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 0
    expect_2 = 0
    # Solve Part 1
    answer1 = part1(input_data)
    if answer1 is not None:
        print(f"Part 1 Answer: {{answer1}}")
        assert answer1 == expect_1

        # Uncomment the following line to submit Part 1 answer
        # submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {{answer2}}")
        assert answer2 == expect_2

        # Uncomment the following line to submit Part 2 answer
        # submit(answer2, part='b', year=year, day=day)
