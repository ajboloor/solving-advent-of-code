with open('input.txt', 'r') as f:
    data = f.read()

# ground_truth = 157

items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = range(1, 52+1)

items, priority = list(items), list(priority)
assert len(items) == 26*2
assert len(priority) == 26*2

priority_dict = dict(zip(items, priority))


## Part 1
priority_sum = 0
for line in data.split('\n'):
    bagsize = len(line)
    bag1, bag2 = line[:bagsize//2], line[bagsize//2:]
    bag1, bag2 = set(bag1), set(bag2)

    common_item = bag1.intersection(bag2)

    if len(common_item) != 0:
        priority_sum += priority_dict[common_item.pop()]
print("Part 1:", priority_sum)

## Part 2
priority_sum = 0
bag_group = []
for i, bag in enumerate(data.split('\n')):
    bag_group.append(bag)

    if (i+1) % 3 == 0 and i != 0:
        bag1, bag2, bag3 = bag_group[0], bag_group[1], bag_group[2]
        bag1, bag2, bag3 = set(bag1), set(bag2), set(bag3)
        common_item = bag1.intersection(bag2).intersection(bag3)

        if len(common_item) != 0:
            priority_sum += priority_dict[common_item.pop()]
        bag_group = []
print("Part 2:", priority_sum)