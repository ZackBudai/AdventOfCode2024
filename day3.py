import re

#PART 1:
# Open the file in read mode
with open('day3.txt', 'r') as file:
    # Read the contents of the file
    data = file.read().splitlines()
result = 0
# Print the contents of the file
for row in data:
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', row)
    for match in matches:
        num1, num2 = map(int, match)
        result += (num1 * num2)
print(result)

#PART 2:
with open('day3.txt', 'r') as file:
    # Read the contents of the file
    data = file.read().splitlines()
mul_regex = re.compile(r"mul\((\d+),(\d+)\)")
do_regex = re.compile(r"do\(\)")
dont_regex = re.compile(r"don't\(\)")
enabled = True
result = 0
for row in data:
    for match in re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", row):
        instruction = match.group(0)
        if do_regex.fullmatch(instruction):
            enabled = True
        elif dont_regex.fullmatch(instruction):
            enabled = False
        elif mul_regex.fullmatch(instruction) and enabled:
            x, y = map(int, mul_regex.match(instruction).groups())
            result += x * y
print(result)