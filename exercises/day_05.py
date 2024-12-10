"""
Advent of Code 2024 - Day 5
"""
import pytest
# class Ordering:
#     def __init__(self):
#         self.orders = {}
#
#     def add_order(self, order):
#         if isinstance(order, Order):
#             self.orders.append(order)
#         else:
#             raise ValueError("Only Order objects can be added")
#     def add_pre_to_post(self,pre,post):
#
#     def get_original(self):
#         return self.orders
#
#     def get_sorted_asc(self):
#         return sorted(self.orders, key=lambda order: order.pre)
#
#     def get_sorted_desc(self):
#         return sorted(self.orders, key=lambda order: order.pre, reverse=True)
#
#     def __repr__(self):
#         if not self.orders:
#             return "Ordering: No orders have been added yet."
#         orders_repr = "\n".join([f" {order}" for order in self.orders])
#         return f"Ordering:\n{orders_repr}"
#     def __str__(self):
#         return self.__repr__()
#
#     def format_sorted(self, sorted_list):
#         if not sorted_list:
#             return "Ordering: No orders have been added yet."
#         orders_repr = "\n".join([f"  {order}" for order in sorted_list])
#         return f"Ordering:\n{orders_repr}"
#
# class Order:
#     def __init__(self, pre,post):
#         self.post = post
#         self.pre = [pre]
#     def add_post_to_pre(self, pre,post):
#         self.post.append(pre)
#
#     def __repr__(self):
#         return f"pre: {self.pre} | post: {self.post}"
#
#     def __eq__(self, other):
#         return self.pre == other.pre and self.post == other.post
#     def __lt__(self, other):
#         return self.pre < other.pre
def add_to_dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []  # Initialize with an empty list if the key doesn't exist
    dictionary[key].append(value)  # Append the value to the list

def get_middle_element_even(lst):
    if not lst:
        return 0  # Return a default value for empty lists
    mid_index = len(lst) // 2
    if len(lst) % 2 == 0:
        return lst[mid_index - 1]
    else:
        return lst[mid_index]

s = "\n----------------------\n"
def part1(input_data):
    # input_data = '47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47'
    input_data = input_data.split('\n\n')
    rules_raw = input_data[0].split('\n')
    print(f"{rules_raw=}")
    lines = input_data[1].split('\n')
    post_pre = {}
    pre_post = {}
    r = []
    for line in rules_raw:
        rule = line.split('|')
        r1 = int(rule[0])
        r2 = int(rule[1])
        # print(rule)
        add_to_dict(pre_post, r1, r2)
        add_to_dict(post_pre, r2, r1)
    # print(f"{r=}")
    # print(f"Original Orders:\n{ordering}")
    print(f"{post_pre=}")
    print(f"{pre_post=}")
    # print(f"Sorted Descending:\n{ordering.format_sorted(ordering.get_sorted_desc())}")
    # print(f"{s}RULES: {len(r)}")

    print(f"LINES: {len(lines)}{s}")
    middle = 0
    for i,pages in enumerate(lines):
        print(f"{i:4}: {pages=}")
        pages = pages.split(',')
        pages = [int(page) for page in pages]

        prev_page = 0
        contain_error = False
        for j,page in enumerate(pages):
            if j == 0:
                continue
            prev_page = int(pages[j-1])
            print(f"{i:4} | {j:4} | {prev_page=} | {page=}")

            correct = prev_page in post_pre.get(page, [])
            wrong = not(correct)
            print(f"{i:4} | {j:4} | {prev_page=} | {page=} | {correct=}")
            if wrong:
                print(f"{i:4} | {j:4} | {prev_page=} | {page=} | {correct=} ERROR -----------------")

                contain_error = True
                break
        if not contain_error:
            middle += get_middle_element_even(pages)
    print(f"{middle=}")
    return middle
def reorder_pages(pages, rules):
    from collections import defaultdict, deque

    # Dependency graph
    in_degree = defaultdict(int)
    graph = defaultdict(list)

    for key, values in rules.items():
        for value in values:
            graph[key].append(value)
            in_degree[value] += 1

    # Queue for topological sorting
    queue = deque([page for page in pages if in_degree[page] == 0])
    ordered_pages = []

    # Topological sorting
    while queue:
        current = queue.popleft()
        ordered_pages.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0 and neighbor in pages:
                queue.append(neighbor)

    # Ensure all pages are included, even if not part of dependencies
    remaining_pages = [page for page in pages if page not in ordered_pages]
    ordered_pages.extend(remaining_pages)

    return ordered_pages
from collections import defaultdict

def part2(input_data):
    input_data = '47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47'

    p1, p2 = input_data.split('\n\n')

    for p in p2.split('\n'):
        print(f"{p=}")
    updates = [list(map(int, line.split(','))) for line in p2.splitlines()]

    orders = defaultdict(list)
    for order in p1.splitlines():
        before, after = order.split('|')
        orders[int(before)].append(int(after))
    print(f"{orders=}")
    part1 = 0
    part2 = 0
    for pages in updates:
        sorted_pages = sorted(pages, key=lambda page: -len([order for order in orders[page] if order in pages]))
        print(f"sorted_pages={sorted_pages}")
        if pages == sorted_pages:
            part1 += pages[len(pages) // 2]
        else:
            part2 += sorted_pages[len(sorted_pages) // 2]
    print('--Part 1', part1)
    print('--Part 2', part2)

    return part2



if __name__ == "__main__":
    from aocd import submit, post
    from aocd.models import Puzzle

    year = 2024
    day = 5
    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data
    expect_1 = 0
    expect_2 = 0
    # Solve Part 1
    # answer1 = part1(input_data)
    # if answer1 is not None:
    #     print(f"Part 1 Answer: {answer1}")
    #     #assert answer1 == expect_1
    #
    #     # Uncomment the following line to submit Part 1 answer
    #     submit(answer1, part='a', year=year, day=day)

    # Solve Part 2
    answer2 = part2(input_data)
    if answer2 is not None:
        print(f"Part 2 Answer: {answer2}")
        #assert answer2 == expect_2

        # Uncomment the following line to submit Part 2 answer
        submit(answer2, part='b', year=year, day=day)
