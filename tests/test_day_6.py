# test_day_06.py

import pytest
from exercises.day_06_1 import part1, part2

# List of examples: (input_data, expected_answer_a, expected_answer_b)
examples = [
    ('....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...', '41', None),
]

@pytest.mark.parametrize("input_data, expected_a, expected_b", examples)
def test_part1(input_data, expected_a, expected_b):
    assert part1(input_data) == expected_a

@pytest.mark.parametrize("input_data, expected_a, expected_b", examples)
def test_part2(input_data, expected_a, expected_b):
    assert part2(input_data) == expected_b
