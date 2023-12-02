import re

with open("input", "r") as file:
    buffer = file.read()
    lines = buffer.splitlines()

p1 = 0
p2 = 0

for line in lines:
    colours = {"red": 0, "green": 0, "blue": 0}
    gameid = line.split(":")[0].split(' ')[1]
    results = re.split(r"; |, ", line[7+len(gameid):])
    for result in results:
        result = result.split(' ')
        if int(result[0]) > colours[result[1]]:
            colours[result[1]] = int(result[0])

    if all((colours["red"] <= 12, colours["green"] <= 13, colours["blue"] <= 14)):
        p1 += int(gameid)
    
    p2 += colours["red"] * colours["green"] * colours["blue"]

print(f"Part One Solution: {p1}")
print(f"Part Two Solution: {p2}")