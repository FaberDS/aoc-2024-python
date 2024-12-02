import os
import webbrowser
from aocd.models import Puzzle

def setup_aoc_day(year, day, template_path, test_template_path, exercises_dir='exercises', tests_dir='tests'):
    # Create necessary directories if they don't exist
    os.makedirs(exercises_dir, exist_ok=True)
    os.makedirs(tests_dir, exist_ok=True)
    init_file_path = os.path.join(exercises_dir, '__init__.py')
    if not os.path.exists(init_file_path):
        with open(init_file_path, 'w') as init_file:
            init_file.write("# This file allows the directory to be recognized as a Python package.\n")

    # Create a Puzzle instance
    puzzle = Puzzle(year=year, day=day)

    # Fetch the puzzle description
    description_html = puzzle._get_prose()

    # Define the HTML file path
    html_file_path = os.path.join(exercises_dir, f'day_{day:02d}_description.html')

    # Write the HTML content to the file
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(description_html)

    # Open the HTML file in the default web browser
    webbrowser.open(f'file://{os.path.abspath(html_file_path)}')

    # Read the solution template content
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    # Replace placeholders with actual values
    script_content = template_content.format(year=year, day=day)

    # Define the Python script file path
    script_file_path = os.path.join(exercises_dir, f'day_{day:02d}.py')

    # Write the Python script content to the file
    with open(script_file_path, 'w', encoding='utf-8') as script_file:
        script_file.write(script_content)

    # Generate test script
    generate_test_script(puzzle, day, test_template_path, tests_dir)

    print(f"Setup complete for Day {day}, {year}.")
    print(f"Description saved to: {html_file_path}")
    print(f"Script created: {script_file_path}")

def generate_test_script(puzzle, day, test_template_path, tests_dir):
    # Read the test template content
    with open(test_template_path, 'r', encoding='utf-8') as test_template_file:
        test_template_content = test_template_file.read()

    # Prepare the examples in the required format
    example_lines = []
    for example in puzzle.examples:
        line = f"    ({repr(example.input_data)}, {repr(example.answer_a)}, {repr(example.answer_b)}),"
        example_lines.append(line)
    examples_str = "\n".join(example_lines)

    # Insert the examples into the test template
    test_code = test_template_content.format(day=day, examples=examples_str)

    # Define the test script file path
    test_script_file_path = os.path.join(tests_dir, f'test_day_{day}.py')

    # Write the test code to the test script file
    with open(test_script_file_path, 'w', encoding='utf-8') as test_script_file:
        test_script_file.write(test_code)

    print(f"Test cases created: {test_script_file_path}")


if __name__ == "__main__":
    import argparse

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Setup Advent of Code day.")
    parser.add_argument("year", type=int, help="Year of the AoC challenge")
    parser.add_argument("day", type=int, help="Day of the AoC challenge")
    parser.add_argument(
        "-t", "--template", default="templates/aoc_template.py",
        help="Path to the solution template Python file"
    )
    parser.add_argument(
        "-tt", "--test_template", default="templates/test_template.py",
        help="Path to the test template Python file"
    )
    parser.add_argument(
        "-e", "--exercises_dir", default="exercises",
        help="Directory to store all exercise files"
    )
    parser.add_argument(
        "-ts", "--tests_dir", default="tests",
        help="Directory to store all test files"
    )

    args = parser.parse_args()

    # Call the setup function with provided arguments
    setup_aoc_day(args.year, args.day, args.template, args.test_template, args.exercises_dir, args.tests_dir)
