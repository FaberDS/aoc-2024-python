"""
Advent of Code 2024 - Day 8
"""
import pytest
import re
from collections import defaultdict
from itertools import combinations
from math import gcd

def print_rows(rows):
    for row in rows:
        print("".join(row))

def part1(input_data):
    #input_data  = '............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............'
    rows = [list(row) for row in input_data.splitlines()]
    print_rows(rows)

    row_lengths = [len(row) for row in rows]
    row_count = len(row_lengths)
    column_count = row_lengths[0]
    print(f"{row_count=} | {column_count=}")

    antennas = defaultdict(list)
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c.isalnum():
                antennas[c].append([x, y])

    print(f"{antennas=}")

    antinodes = set()

    for antenna, coordinates in antennas.items():
        print(f"{antenna=} {coordinates=}")
        for a, b in combinations(coordinates, 2):
            print(f"{a=} {b=} combinations")

            diff_x = b[0] - a[0]
            diff_y = b[1] - a[1]

            possible_antinode_1 = [a[0] - diff_x, a[1] - diff_y]
            possible_antinode_2 = [b[0] + diff_x, b[1] + diff_y]

            for p_antinode in [possible_antinode_1, possible_antinode_2]:
                x, y = p_antinode
                if 0 <= x < column_count and 0 <= y < row_count:
                    # Mark as an antinode if it is within bounds
                    antinodes.add((x, y))
                    if rows[y][x] == '.':
                        rows[y][x] = '#'

    # Print updated map and return the number of unique antinodes
    print("Updated Map:")
    print_rows(rows)

    print(f"Total unique antinodes: {len(antinodes)}")
    return len(antinodes)


def part2(input_data):
    # input_data  = '............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............'
    rows = [list(row) for row in input_data.splitlines()]
    print_rows(rows)

    row_lengths = [len(row) for row in rows]
    row_count = len(row_lengths)
    column_count = row_lengths[0]
    print(f"{row_count=} | {column_count=}")
    antinodes = set()

    antennas = defaultdict(list)
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c.isalnum():
                antennas[c].append([x, y])
                antinodes.add((x, y))

    print(f"{antennas=}")

    for antenna, coordinates in antennas.items():
        print(f"{antenna=} {coordinates=}")
        for a, b in combinations(coordinates, 2):
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            print(f"{a=} {b=} {dx=} {dy=}")
            queue = [(a[0] - dx, a[1] - dy), (b[0] + dx, b[1] + dy)]
            visited = set(queue)

            while queue:
                x, y = queue.pop(0)
                print(f"{x=} {y=} | {queue=}")
                if 0 <= x < column_count and 0 <= y < row_count:
                    antinodes.add((x, y))

                    if rows[y][x] == '.':
                        rows[y][x] = '#'

                    next_antinode1 = (x - dx, y - dy)
                    next_antinode2 = (x + dx, y + dy)

                    for next_antinode in (next_antinode1, next_antinode2):
                        if (
                                0 <= next_antinode[0] < column_count
                                and 0 <= next_antinode[1] < row_count
                                and next_antinode not in visited
                        ):
                            visited.add(next_antinode)
                            queue.append(next_antinode)

    print("Updated Map:")
    print_rows(rows)

    print(f"Total unique antinodes: {len(antinodes)}")
    return len(antinodes)

if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 8
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 361
    expect_2 = 1249
    # Solve Part 1
    answer1 = None# part1(input_data)
    if answer1 is not None:
        print(f"Part 1 Answer: {answer1}")
        assert answer1 == expect_1

        # Uncomment the following line to submit Part 1 answer
        submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        assert answer2 == expect_2

        # Uncomment the following line to submit Part 2 answer
        submit(answer2, part='b', year=year, day=day)
