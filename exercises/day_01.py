"""
Advent of Code 2024 - Day 1
"""

def part1(input_data):
    left = []
    right = []

    for line in input_data.split('\n'):
        if line == '':
            continue
        numbers = list(map(int, line.strip().split("   ")))
        left.append(numbers[0])
        right.append(numbers[1])

    left.sort()
    right.sort()

    total_distance = 0
    for i, v_left in enumerate(left):
        v_right = right[i]
        dif = abs(v_left - v_right)
        # print(f"{v_left=} | {v_right=} | {dif=}")
        total_distance += dif
    return f"{total_distance}"

def part2(input_data):
    left = []
    right = []

    for line in input_data.split('\n'):
        if line == '':
            continue
        numbers = list(map(int, line.strip().split("   ")))
        left.append(numbers[0])
        right.append(numbers[1])
    # print(f"{left=}")
    # print(f"{right=}")
    total_similarity = 0
    for v_left in left:
        count = len(list(filter(lambda v: v == v_left, right)))
        similarity = count * v_left
        total_similarity += similarity
        # print(f"{v_left=} {count=} {similarity=} {total_similarity=}")
    return f"{total_similarity}"

if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 1
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data

    # Solve Part 1
    answer1 = part1(input_data)
    if answer1 is not None:
        print(f"Part 1 Answer: {answer1}")
        # Uncomment the following line to submit Part 1 answer
        #åååsubmit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        # Uncomment the following line to submit Part 2 answer
        # submit(answer2, part='b', year=year, day=day)
