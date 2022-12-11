with open('input.txt', 'r') as f:
    data = f.read()

## Part 1
enclosed_pairs = 0
for line in data.split('\n'):
    elf1, elf2 = line.split(',')
    elf1, elf2 = elf1.split('-'), elf2.split('-')
    elf1_min, elf1_max = int(elf1[0]), int(elf1[1])    
    elf2_min, elf2_max = int(elf2[0]), int(elf2[1])

    # elf2 enclosed in elf1
    cond1 = (elf2_min >= elf1_min) and (elf2_max <= elf1_max)
    
    # elf1 enclosed in elf2
    cond2 = (elf1_min >= elf2_min) and (elf1_max <= elf2_max)
    
    if cond1 or cond2:
        enclosed_pairs += 1
print("Part 1:", enclosed_pairs)

## Part 2
overlapping_pairs = 0
for line in data.split('\n'):
    elf1, elf2 = line.split(',')
    elf1, elf2 = elf1.split('-'), elf2.split('-')
    elf1_min, elf1_max = int(elf1[0]), int(elf1[1])    
    elf2_min, elf2_max = int(elf2[0]), int(elf2[1])

    # elf2 not overlapping elf1
    cond1 = (elf2_min > elf1_max)

    # elf1 not overlapping elf2
    cond2 = (elf1_min > elf2_max)

    if not(cond1 or cond2):
        overlapping_pairs += 1
print("Part 2:", overlapping_pairs)
