
with open("input", 'r') as file:
    buffer = file.read().replace("  ", " ")
    lines = [x.split(': ')[1] for x in buffer.splitlines()]

p1 = 0

headache = {x: 1 for x in range(len(lines))}

for i, line in enumerate(lines):
    i += 1
    parts = line.split(' | ')
    winningnumbers = set(int(x) for x in parts[0].split(' '))
    numberspresent = set(int(x) for x in parts[1].split(' '))
    correctnumbers = len(winningnumbers & numberspresent)

    if correctnumbers > 0:
        p1 += 2**(correctnumbers-1)
    
    for x in range(i, min(len(lines), i + correctnumbers)):
        headache[x] += headache[i-1]
    
p2 = sum(headache.values())


print(f"Part One Solution: {p1}")
print(f"Part Two Solution: {p2}")
