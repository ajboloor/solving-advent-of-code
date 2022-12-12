
def parse_data(filename):
    """
    return
    1. list of stacks for the crates
    2. list of movements like [num_crates, from, to]
    """
    with open(filename, 'r') as f:
        data = f.read()
    crate_data, instructions = data.split('\n\n')

    num_stacks = int(crate_data.split('\n')[-1].strip().split(' ')[-1])
    
    spacing = 4
    indices = list(range(1, 1+spacing*num_stacks, spacing))

    crate_stacks = []
    for _ in range(num_stacks):
        crate_stacks.append([])


    for line in crate_data.split('\n')[::-1][1:]:
        for crate_id, idx in enumerate(indices):
            if line[idx] != ' ':
                crate_stacks[crate_id].append(line[idx])
    # print("crate_stacks:", crate_stacks)
    return crate_stacks, instructions



## Part 1
crate_stacks, instructions = parse_data('input_mini.txt')

for instruction in instructions.split('\n'):
    move_num = int(instruction.split('move ')[1].split(' ')[0])
    move_from = int(instruction.split('from ')[1].split(' ')[0])
    move_to = int(instruction.split('to ')[1])

    for move in range(move_num):
        crate = crate_stacks[move_from-1].pop()
        crate_stacks[move_to-1].append(crate)

output = ''
for i in range(len(crate_stacks)):
    output += crate_stacks[i].pop()
print("Part 1", output)

## Part 2
crate_stacks, instructions = parse_data('input.txt')

for instruction in instructions.split('\n'):
    move_num = int(instruction.split('move ')[1].split(' ')[0])
    move_from = int(instruction.split('from ')[1].split(' ')[0])
    move_to = int(instruction.split('to ')[1])

    curr_stack = []
    for move in range(move_num):
        curr_stack.append(crate_stacks[move_from-1].pop())
    for move in range(move_num):
        crate_stacks[move_to-1].append(curr_stack.pop())

output = ''
for i in range(len(crate_stacks)):
    output += crate_stacks[i].pop()
print("Part 2", output)