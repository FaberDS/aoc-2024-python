"""
Advent of Code 2024 - Day 6
"""
import pytest
from enum import Enum
from collections import namedtuple
import copy

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
    OBSTRUCTION = 'O'

class OutOfMapException(Exception):
    pass

class OneObstructionIsNotEnough(Exception):
    pass
class ReachedObstruction(Exception):
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
    print_map(map)
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
    obstruction_count = 0
    try:
        while True:
            # print(f"global Count: {round}")

            try:
                find_exit(map,position,direction)
            except ReachedObstruction:
                obstruction_count += 1
                # print(f"ReachedObstruction at {position=} | {obstruction_count=}")
            except OneObstructionIsNotEnough:
                pass
            next_step = get_next_step(map,position,direction)

            map = next_step[0]
            direction = next_step[1]
            position = next_step[2]
            round += 1
    except OutOfMapException:
        pass
        # print(f"OutOfMapException at {position=}")


    print_map(map)
    print(f"{obstruction_count=}")
    # unique_position_count = 0
    # for row in map:
    #     for p in row:
    #         if p == Field_Type.CURSOR.value:
    #             unique_position_count += 1
    return obstruction_count

def find_exit(map, position, direction):
    possible_next_position = check_next_field(map,position,direction)
    new_map = copy.deepcopy(map)

    if possible_next_position is None:
        raise OutOfMapException
    elif possible_next_position.field_type == Field_Type.GUARD:
        # If there is a guard there is no need for a new obstruction
        return
    elif possible_next_position.field_type == Field_Type.FREE or possible_next_position.field_type == Field_Type.CURSOR:
        new_map = set_value_for_position(new_map, possible_next_position,Field_Type.OBSTRUCTION)
    elif possible_next_position.field_type == Field_Type.OBSTRUCTION:
        raise ReachedObstruction()
    placed_obstruction = False
    init_position = position
    direction = turn(direction) # Turn to see if an obstruction upfront would lead to a circle
    round = 1
    while True:

        # print_map(new_map)
        try:
            next_step = get_next_step(new_map,position,direction)
        except OutOfMapException:
            raise OneObstructionIsNotEnough()
        new_map = next_step[0]
        direction = next_step[1]
        position = next_step[2]
        new_field_type = next_step[3]

        if new_field_type is not None and new_field_type is Field_Type.OBSTRUCTION.value:
            raise ReachedObstruction()
        round += 1

def get_value_for_coordinate(map, coordinate):
    return map[coordinate.y][coordinate.x]

def get_value_for_position(map, position):
    return map[position.y][position.x]

def set_value_for_position(map, position, field_type):
    map[position.y][position.x] = field_type.value
    return map


def get_next_step(map, position,direction):
    next_position = check_next_field(map,position,direction)
    # print(f"{next_position=}")
    # print(f"{next_position.field_type=}")
    field_type = None
    if next_position.field_type == Field_Type.GUARD:
        while True:
            # print(f"{next_position=} FOUND GUARD")
            direction = turn(direction)
            next_position = get_next_coordinates(position.x,position.y,direction)
            next_field_type = get_value_for_position(map, next_position)
            if next_field_type != Field_Type.GUARD:
                break
    field_type = get_value_for_position(map, next_position)
    map = set_value_for_position(map,next_position,Field_Type.CURSOR)
    return (map,direction, next_position, field_type)

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

def check_next_field(map,current_coordinates,direction):
    coordinates = get_next_coordinates(current_coordinates.x, current_coordinates.y,direction)
    # print(f"{x=} | {y=} | {direction=} | {coordinates=}")

    x = coordinates.x
    y = coordinates.y

    # print(f"{x=} | {y=} | {direction=} UPDATE")
    if not is_on_map(map,x,y):
        raise OutOfMapException()
    return Position(x=x,y=y,field_type=Field_Type(get_value_for_coordinate(map,coordinates)))

def is_on_map(map,x,y):
    if x < 0 or y < 0:
        return False
    if x >= len(map):
        return False
    if y >= len(map[0]):
        return False
    return True


# def part2(input_data):
#     # input_data = '....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...'
#     map = [list(row) for row in input_data.split('\n')]
#     result = evaluate_map(map)
#     print(f"{result=}")
#     result
#     pass
def find_guard_start(map):
    for r, row in enumerate(map):
        for c, cell in enumerate(row):
            if cell in {Field_Type.CURSOR.value}:
                return Coordinate(c, r), Direction.NORTH  # Adjust based on the facing direction
    return None, None

def causes_loop(map, start_position, start_direction):
    visited_states = set()
    position = start_position
    direction = start_direction

    while True:
        # Convert the map to a hashable representation (tuple of tuples)
        state = (position.x, position.y, direction, tuple(tuple(row) for row in map))
        if state in visited_states:
            # Loop detected
            return True
        visited_states.add(state)

        try:
            # Get the next step based on the current position and direction
            next_step = get_next_step(map, position, direction)
        except OutOfMapException:
            # Guard exits the map
            return False

        # Update the map, position, and direction based on the next step
        map = next_step[0]
        direction = next_step[1]
        position = next_step[2]


def part2(input_data):
    input_data = '....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...'

    map = [list(row) for row in input_data.split('\n')]
    start_position, start_direction = find_guard_start(map)
    possible_positions = []

    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == Field_Type.FREE.value:
                # Temporarily place an obstruction
                map[r][c] = Field_Type.OBSTRUCTION.value
                if causes_loop(map, start_position, start_direction):
                    possible_positions.append((c, r))
                # Remove the obstruction
                map[r][c] = Field_Type.FREE.value

    print(f"Possible positions for obstruction: {possible_positions}")
    return len(possible_positions)


if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 6
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_2 = 0

    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        assert answer2 == expect_2

        # Uncomment the following line to submit Part 2 answer
        # submit(answer2, part='b', year=year, day=day)
