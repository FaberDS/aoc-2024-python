# https://adventofcode.com/2024/day/1
left = []
right = []
with open('01_input.txt', 'r') as file:
    for line in file:        
        numbers = list(map(int,line.strip().split("   ")))
        left.append(numbers[0])
        right.append(numbers[1])



left.sort()
right.sort()

total_distance = 0
for i,v_left in enumerate(left):
    v_right = right[i]
    dif = abs(v_left - v_right)
    # print(f"{v_left=} | {v_right=} | {dif=}")
    total_distance += dif

print(f"Part one total_distance {total_distance}")

total_similarity = 0
for v_left in left:
    count = len(list(filter(lambda v: v == v_left, right)))
    similarity = count * v_left
    total_similarity += similarity

print(f"Part two total_similarity {total_similarity}")