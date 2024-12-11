# test_day_11.py

import pytest
from exercises.day_11 import part1, part2

# List of examples: (input_data, expected_answer_a, expected_answer_b)
examples = [
    ('125 17', 55312),
]

@pytest.mark.parametrize("input_data, expected_a", examples)
def test_part1(input_data, expected_a):
    assert part1(input_data) == expected_a

