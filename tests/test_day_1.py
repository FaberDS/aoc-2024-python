# test_day_01.py

import pytest
from exercises.day_01 import part1, part2

# List of examples: (input_data, expected_answer_a, expected_answer_b)
examples = [
    ('3   4\n4   3\n2   5\n1   3\n3   9\n3   3', '11', '9'),
]

@pytest.mark.parametrize("input_data, expected_a, expected_b", examples)
def test_part1(input_data, expected_a, expected_b):
    assert part1(input_data) == expected_a

@pytest.mark.parametrize("input_data, expected_a, expected_b", examples)
def test_part2(input_data, expected_a, expected_b):
    assert part2(input_data) == expected_b
