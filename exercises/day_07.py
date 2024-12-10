"""
Advent of Code 2024 - Day 7
"""
import math
from itertools import product

def find_valid_equations(input_data,operations):
    valid_targets = []
    for target, numbers in input_data.items():
        # print(f"{target=} | {numbers=}")
        num_operators = len(numbers) - 1
        for ops in product(operations, repeat=num_operators):
            if evaluate_expression_part(numbers, ops) == target:
                valid_targets.append(target)
                break
    return (sum(valid_targets), valid_targets)


def evaluate_expression_part(numbers, operators):
    result = numbers[0]
    # print(f"evaluate_expression_part_2 {numbers=} | {operators=}")

    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '|':
            result = int(str(result) + str(numbers[i + 1]))
    # print(f"evaluate | {numbers=} | {operators=} | {result=}")

    return result
def part1(input_data):
    # input_data = '190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20'
    lines = input_data.split('\n')
    print(f"PART-1 {len(lines)} lines found")
    equations = {}
    correct_lines = []
    for line in lines:
        key, values = line.split(':')
        key = int(key.strip())
        values = list(map(int, values.strip().split()))
        equations[key] = values
    # print(equations)
    result = find_valid_equations(equations, '+*')
    correct_sum = result[0]
    correct_lines = result[1]

    # print(f"{correct_sum=} | {len(correct_lines)= }/ {len(equations)=}")
    return correct_sum

def part2(input_data):
    # input_data = '190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20'
    lines = input_data.split('\n')
    print(f"PART-2 {len(lines)} lines found")

    # print(f"{len(lines)} lines found")
    equations = {}
    correct_lines = []
    for line in lines:
        key, values = line.split(':')
        key = int(key.strip())
        values = list(map(int, values.strip().split()))
        equations[key] = values
    # print(equations)

    result = find_valid_equations(equations,'+*|')
    correct_sum = result[0]
    correct_lines = result[1]
    # print(f"{correct_sum=} | {len(correct_lines)= }/ {len(equations)=}")
    return correct_sum


if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 7
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 932137732557
    expect_2 = 661823605105500
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
