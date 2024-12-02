#https://adventofcode.com/2024/day/2
reports = []
with open('02_input.txt', 'r') as file:
    for line in file:        
        numbers = list(map(int,line.strip().split(" ")))
        reports.append(numbers)

print(f"{reports=}")

def all_values_are_decreasing(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:  
            return False
    return True

 
def all_values_are_increasing(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:  
            return False
    return True

def difference_is_one_and_three(numbers):
    for i,num in enumerate(numbers):
        if i == 0:
            continue
        previous = numbers[i-1]
        difference = abs(num-previous)
        if not(difference >= 1 and difference <= 3):
            return False

    return True
 
def is_safe_report(report):
    if (all_values_are_increasing(report) or all_values_are_decreasing(report)) and difference_is_one_and_three(report):
        return True
    return False

def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True
    return False

safe_reports = []
for report in reports:
    if is_safe_report(report) or is_safe_with_dampener(report):
        safe_reports.append(report)

print(f"Total Reports: {len(reports)} | Safe Reports: {len(safe_reports)}")