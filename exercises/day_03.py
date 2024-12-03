"""
Advent of Code 2024 - Day 3
"""
import re
from collections import Counter

def part1(input_data):
    print(input_data)
    pattern = r'mul\((\d+,\d+)\)'
    matches = re.findall(pattern, input_data)

    result = 0
    for match in matches:
        numbers = list(map(int,match.split(',')))
        result += numbers[0] * numbers[1]
    return result

def part2(input_data):
    input_data = input_data.replace("’", "'").replace("‘", "'").strip()
    pattern = r"(don't\(\)|do\(\)|mul\(\d+,\d+\))"

    matches = re.findall(pattern, input_data)

    result = 0
    should_multiply = True
    for i,match in enumerate(matches):
        if match == 'do()' and not should_multiply:
            should_multiply = True
        elif match == "don't()" and should_multiply:
            should_multiply = False
        elif should_multiply:
            pattern = r"mul\((\d+,\d+)\)"
            n_matches = re.findall(pattern, match)
            numbers = []
            for n_match in n_matches:
                numbers = list(map(int, n_match.split(',')))
            if len(numbers) == 2:
                result += numbers[0] * numbers[1]
    return result

if __name__ == "__main__":
    import sys
    import re

    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 3
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data

    #Solve Part 1
    answer1 = part1(input_data)
    if answer1 is not None:
        print(f"Part 1 Answer: {answer1}")
        # Uncomment the following line to submit Part 1 answer
    #     submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        # Uncomment the following line to submit Part 2 answer
        #submit(answer2, part='b', year=year, day=day)
