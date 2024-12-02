# test_day_{day:02d}.py

import pytest
from exercises.day_{day:02d} import part1, part2

# List of examples: (input_data, expected_answer_a, expected_answer_b)
examples = [
{examples}
]

@pytest.mark.parametrize("input_data, expected_a, expected_b", examples)
def test_part1(input_data, expected_a, expected_b):
    assert part1(input_data) == expected_a

@pytest.mark.parametrize("input_data, expected_a, expected_b", examples)
def test_part2(input_data, expected_a, expected_b):
    assert part2(input_data) == expected_b
