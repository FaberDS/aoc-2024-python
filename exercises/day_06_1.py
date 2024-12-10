"""
Advent of Code 2024 - Day 6
"""
import pytest
from enum import Enum
from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['x', 'y'])
Position = namedtuple('Position', ['x','y', 'field_type'])

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Field_Type(Enum):
    CURSOR = '^'
    GUARD = '#'
    FREE = '.'
    OUT_OF_MAP = ""

class OutOfMapException(Exception):
    pass

def turn(direction):
    new_direction_index = direction.value + 1
    if new_direction_index == len(Direction):
        return Direction(0)
    return Direction(new_direction_index)

def print_map(map):
    for row in map:
        print(row)

def evaluate_map(map):
    direction = Direction.NORTH
    # print_map(map)
    position = None
    for r, row in enumerate(map):
        for c, column in enumerate(row):
            x = c
            y = r
            current_field_type = Field_Type(map[r][c])
            if current_field_type == Field_Type.CURSOR:
                position = Coordinate(x, y)
                break
        if position is not None:
            break
    print(f"POSITION:\n{position}")
    round = 1

    try:
        while True:
            # print(f"Count: {round}")
            # print_map(map)
            next_step = get_next_step(map,position,direction)
            if next_step is None:
                raise OutOfMapException()
            map = next_step[0]
            direction = next_step[1]
            position = next_step[2]
            round += 1

    except OutOfMapException:
        print(f"Got out in {round} rounds.")
    print_map(map)
    unique_position_count = 0
    for row in map:
        for p in row:
            if p == Field_Type.CURSOR.value:
                unique_position_count += 1
    return unique_position_count

def get_value_for_position(map, position):
    return map[position.y][position.x]


def get_next_step(map, position,direction):
    next_position = check_next_field(map,position.x,position.y,direction)
    if next_position.field_type == Field_Type.OUT_OF_MAP:
        return
    # print(f"{next_position=}")
    # print(f"{next_position.field_type=}")
    if next_position.field_type == Field_Type.GUARD:
        while True:
            # print(f"{next_position=} FOUND GUARD")
            direction = turn(direction)
            next_position = get_next_coordinates(position.x,position.y,direction)
            next_field_type = get_value_for_position(map, next_position)
            if next_field_type != Field_Type.GUARD:
                break
    map = instert_new_position(map,next_position)
    return (map,direction, next_position)

def instert_new_position(map,next_position):
    # print(f"instert_new_position\n{next_position=}")
    # print_map(map)
    # print(f"{map[next_position.x][next_position.y]=}")
    # print(f"{Field_Type.CURSOR.value=}")
    # print(type(map[next_position.x]))
    # print(map[next_position.x])

    map[next_position.y][next_position.x] = Field_Type.CURSOR.value
    # print_map(map)

    return map

def get_next_coordinates(x,y,direction):
    match direction:
        case Direction.NORTH:
            y = y - 1
        case Direction.EAST:
            x = x + 1
        case Direction.SOUTH:
            y = y + 1
        case Direction.WEST:
            x = x - 1
    return Coordinate(x,y)

def check_next_field(map,x,y,direction):
    coordinates = get_next_coordinates(x,y,direction)
    # print(f"{x=} | {y=} | {direction=} | {coordinates=}")

    x = coordinates.x
    y = coordinates.y

    # print(f"{x=} | {y=} | {direction=} UPDATE")
    if not is_on_map(map,x,y):
        return Position(x=x,y=y,field_type=Field_Type.OUT_OF_MAP)
    return Position(x=x,y=y,field_type=Field_Type(map[y][x]))

def is_on_map(map,x,y):
    if x < 0 or y < 0:
        return False
    if x >= len(map):
        return False
    if y >= len(map[0]):
        return False
    return True



def part1(input_data):
    map = [list(row) for row in input_data.split('\n')]
    result = evaluate_map(map)
    print(f"{result=}")
    result

def part2(input_data):
    # TODO: Implement Part 2 solution
    pass

if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 6
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 4977
    expect_2 = 0
    # Solve Part 1
    answer1 = part1(input_data)
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
        # submit(answer2, part='b', year=year, day=day)
