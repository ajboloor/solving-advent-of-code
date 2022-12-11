"""
assumptions data values are natural numbers
- can they be zero?
-- assume they can

goal
- find cluster with max sum
-- return that sum
"""

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()


    ### Part 1
    max_sum = 0
    cur_sum = 0
    for item in data.split('\n'):
        if item != '':
            value = int(item)
            cur_sum += value
        else:
            if cur_sum > max_sum:
                max_sum = cur_sum
            cur_sum = 0
    print("Part 1:", max_sum)
    with open('sol_part1.txt', 'w') as f:
        f.write(str(max_sum))

    ### Part 2
    max_sum = 0
    cur_sum = 0
    sums = []
    for item in data.split('\n'):
        if item != '':
            value = int(item)
            cur_sum += value
        else:
            if cur_sum > max_sum:
                max_sum = cur_sum
            sums.append(cur_sum)
            cur_sum = 0
    output = sum(sorted(sums)[-3:])
    print("Part 2:", output)
    with open('sol_part2.txt', 'w') as f:
        f.write(str(output))