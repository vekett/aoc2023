import re

conversion = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

with open("input", "r") as file:
    buffer = file.read()
    lines = buffer.splitlines()

def solve(inp):
    inp = re.sub('\D', '', line) # remove any non-digit character
    value = inp[:1] + inp[-1:] # add together the first and last character of the line
    return int(value) # return the final value represented as an integer

p1 = 0
for line in lines:
    p1 += solve(line)

p2 = 0
for line in lines:
    for key, value in conversion.items():
        line = line.replace(key, value)
    
    p2 += solve(line)

print(f"Part One Solution: {p1}")
print(f"Part Two Solution: {p2}")


