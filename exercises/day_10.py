"""
Advent of Code 2024 - Day 10
"""
import copy
from typing import DefaultDict

import utils.parser
from utils import *
import pytest
from collections import defaultdict

from utils import cli_utils


class Trail:
    def __init__(self, start_coordinate, current_coordinate, altitude, path=None):
        self.start_coordinate = start_coordinate
        self.coordinates = current_coordinate
        self.altitude = altitude
        if path is None:
            self.path = (start_coordinate,)
        else:
            self.path = tuple(path)

    def __repr__(self):
        return f"TRAIL start: {self.start_coordinate} alt {self.altitude} history: {self.path}"
    # def print_history(self):
    #     print(f"")
    #     for coordinate in self.path:
    #         print(coordinate)
    def extend(self, new_coordinate, new_altitude):
        # Return a new trail with extended path
        return Trail(
            start_coordinate=self.start_coordinate,
            current_coordinate=new_coordinate,
            altitude=new_altitude,
            path=self.path + (new_coordinate,)
        )

    # def __repr__(self)-> str:
    #     return f"({self.coordinates}-{self.altitude})"
    def is_next_altitude(self,next_altitude):
        return next_altitude == (self.altitude +1)
    # def set_coordinates(self,coordinates, altitude) -> bool:
    #     if not self._is_next_altitude(altitude):
    #         return False
    #     self.coordinates = coordinates
    #     self.altitude += 1
    #     return True

class TrailFinder:
    def __init__(self, topo):
        self.trail_head_count_paths = defaultdict(int)
        self.trail_head_count_unique = {}
        self.topo = topo
        self.topo_size_rows = len(topo)
        self.topo_size_cols = len(topo[0])
        self.trails = []
        self.find_trail_heads()

    def __repr__(self)-> str:
        return f"TRAILFINDER\n{self.trail_head_count_paths=} | {self.topo_size_rows=} | {self.topo_size_cols=}\n"


    def sum_trails_head_count(self) -> int:
        return sum(self.trail_head_count_paths.values())

    def sum_trails_head_count_unique(self) -> int:
        return sum(len(coords) for coords in self.trail_head_count_unique.values())

    def print_topo(self):
        cli_utils.print_map(self.topo)

    def is_valid_coordinate(self, coordinate):
        row, col = coordinate
        return 0 <= row < self.topo_size_rows and 0 <= col < self.topo_size_cols

    def get_valid_neighbors(self,coordinate):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        valid_neighbors = []
        row, col = coordinate

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_coordinate((new_row, new_col)):
                valid_neighbors.append((new_row, new_col))

        return valid_neighbors

    def find_trail_heads(self):
        self.trails = [
            Trail((row_idx, col_idx),(row_idx, col_idx),0)
            for row_idx, row in enumerate(self.topo)
            for col_idx, col in enumerate(row)
            if col == 0
        ]
        self.mark_coordinates(self.trails)

    def get_entry_at(self,coordinate):
        return self.topo[coordinate[0]][coordinate[1]]

    def print_topo_string(self,topo):
        result = "\n".join(["".join(map(str, row)) for row in topo])
        print(result)

    def mark_coordinate(self,coordinates):
        topo_copy = copy.deepcopy(self.topo)
        for coordinate in coordinates:
            row, col = coordinate
            topo_copy[row][col] = '#'
        self.print_topo_string(topo_copy)

    def mark_coordinates(self,trails):
        topo_copy = copy.deepcopy(self.topo)
        print(f"{trails=}")
        for trail in trails:
            row, col = trail.coordinates
            topo_copy[row][col] = '#'
        self.print_topo_string(self.topo)
        self.print_topo_string(topo_copy)


    def find_trails(self):
        while len(self.trails) > 0:
            trail = self.trails.pop()
            valid_neighbors = self.get_valid_neighbors(trail.coordinates)
            # print(f"{trail=} | {valid_neighbors=}")
            for new_row, new_col in valid_neighbors:
                coordinate = (new_row, new_col)
                altitude = self.get_entry_at(coordinate)
                # print(f"\t\tneighbors: {coordinate=} | {new_row=} | {new_col=} | {altitude=} | {trail.is_next_altitude(altitude)}")
                if trail.is_next_altitude(altitude):
                    # print(f"\t\t\tAPPENDED Trail {coordinate=} {altitude=} {trail=} | {self.trails=} ")
                    if altitude == 9:
                        start_coordinates = trail.start_coordinate
                        self.trail_head_count_paths[start_coordinates] += 1
                        if start_coordinates not in self.trail_head_count_unique:
                            self.trail_head_count_unique[start_coordinates] = set()

                        self.trail_head_count_unique[trail.start_coordinate].add(coordinate)
                        # print(trail)
                        self.mark_coordinate(trail.path)
                        # print(f"\t\t\tREACHED: {new_row=} | {new_col=} | {self.sum_trails_head_count()=}")
                    else:
                        new_trail = trail.extend(coordinate, altitude)

                        self.trails.append(new_trail)

                # else:
                #     print(f"\t\t else: {trail=} | {trail.is_next_altitude(altitude)=} {coordinate=}")
        print(f"{self.sum_trails_head_count()=}")
        # for key,value in self.trail_head_count_paths.items():
        #     print(f"{key}: {self.trail_head_count_paths[key]}")
        #
        # print(f"UNIQUE")
        # for key, value in self.trail_head_count_unique.items():
        #     print(f"{key}: {self.trail_head_count_unique[key]}")
        print(f"{self.sum_trails_head_count_unique()}")

def part1(input_data):
    # input_data= '89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732'
    map = utils.parser.split_2d_int_array(input_data)
    trail_finder = TrailFinder(map)
    trail_finder.find_trails()
    return trail_finder.sum_trails_head_count_unique()

def part2(input_data):
    map = utils.parser.split_2d_int_array(input_data)
    trail_finder = TrailFinder(map)
    trail_finder.find_trails()
    return trail_finder.sum_trails_head_count()

if __name__ == "__main__":
    from aocd import submit
    from aocd.models import Puzzle

    year = 2024
    day = 10
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 557
    expect_2 = 1062
    # Solve Part 1
    answer1 = part1(input_data)
    if answer1 is not None:
        print(f"Part 1 Answer: {answer1}")
        # assert answer1 == expect_1

        # Uncomment the following line to submit Part 1 answer
        submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        assert answer2 == expect_2

        # Uncomment the following line to submit Part 2 answer
        submit(answer2, part='b', year=year, day=day)
