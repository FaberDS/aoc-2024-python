"""
Advent of Code 2024 - Day 3
"""
import re
from collections import Counter
import pytest
def part1(input_data):
    print(input_data)
    # More efficient
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input_data)
    result = sum(int(a) * int(b) for a, b in matches)

    return result

    # First Impl
    #pattern = r'mul\((\d+,\d+)\)'
    #matches = re.findall(pattern, input_data)
    # result = 0
    # for match in matches:
    #     numbers = list(map(int,match.split(',')))
    #     result += numbers[0] * numbers[1]
    # return result


def part2(input_data):
    # Refactored
    input_data = input_data.replace("’", "'").replace("‘", "'").strip()

    # Single regex to capture commands and numbers
    pattern = r"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))"
    matches = re.findall(pattern, input_data)

    result, should_multiply = 0, True
    for command, num1, num2 in matches:
        match command:
            case "do()":
                should_multiply = True
            case "don't()":
                should_multiply = False
            case _ if should_multiply and num1 and num2:
                result += int(num1) * int(num2)
    return result

    # First Impl
    # input_data = input_data.replace("’", "'").replace("‘", "'").strip()
    # pattern = r"(don't\(\)|do\(\)|mul\(\d+,\d+\))"
    #
    # matches = re.findall(pattern, input_data)
    #
    # result = 0
    # should_multiply = True
    # for i,match in enumerate(matches):
    #     if match == 'do()' and not should_multiply:
    #         should_multiply = True
    #     elif match == "don't()" and should_multiply:
    #         should_multiply = False
    #     elif should_multiply:
    #         pattern = r"mul\((\d+,\d+)\)"
    #         n_matches = re.findall(pattern, match)
    #         numbers = []
    #         for n_match in n_matches:
    #             numbers = list(map(int, n_match.split(',')))
    #         if len(numbers) == 2:
    #             result += numbers[0] * numbers[1]
    # return result

if __name__ == "__main__":
    import sys
    import re

    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 3
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data

    expect_1 = 155955228
    expect_2 = 100189366
    #Solve Part 1
    answer1 = part1(input_data)
    if answer1 is not None:
        print(f"Part 1 Answer: {answer1}")
        assert answer1 == expect_1

        # Uncomment the following line to submit Part 1 answer
    #     submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        assert answer2 == expect_2
        # Uncomment the following line to submit Part 2 answer
        #submit(answer2, part='b', year=year, day=day)
