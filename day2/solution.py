scoring_part1 = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

scoring_part2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

with open('input.txt', 'r') as f:
    data = f.read()

score = 0
for line in data.split('\n'):
    score += scoring_part1[line]
print("Part 1:", score)
with open('sol_part1.txt', 'w') as f:
    f.write(str(score))

score = 0
for line in data.split('\n'):
    score += scoring_part2[line]
print("Part 2:", score)
with open('sol_part2.txt', 'w') as f:
    f.write(str(score))
