# PART1
import string
rucksack = []
common_item = []
common_item_priority_number = []
with open('day3.txt') as f:
    rucksack = f.read().splitlines()
    for item in rucksack:
        slice_object = slice(int(len(item) /2))
        first_compartment = item[slice(0,int(len(item) /2))]
        second_compartment = item[slice(int(len(item) /2), int(len(item)))]
        for first_cmpt_item in first_compartment:
            for second_compt_item in second_compartment:
                if first_cmpt_item == second_compt_item:
                    common_item.append(first_cmpt_item)
                    break
            else:
                continue
            if first_cmpt_item in common_item:
                if first_cmpt_item.islower():
                    common_item_priority_number.append(string.ascii_lowercase.index(first_cmpt_item) + 1)
                else:
                    common_item_priority_number.append(string.ascii_uppercase.index(first_cmpt_item) + 27)
            break
        else:
            continue



print('Sum for part1 is:', sum(common_item_priority_number))

# Part2:

groups = []
common_char_group = []
common_char_group_priority = []


def getGroup(start):
    return [rucksack[start], rucksack[start+1], rucksack[start+2]]

with open('day3.txt') as f:
    rucksack = f.read().splitlines()
    start = 0
    for item in rucksack:
        groups.append(getGroup(start))
        start = start + 3
        if start > len(rucksack)-1:
            break

for group in groups:
    count = 0 
    # for item_group in group:
    # print(group, 'grouppppp', group[count])
    for first_item in group[count]:
        if first_item in group[count+1] and first_item in group[count+2]:
            common_char_group.append(first_item)
            if first_item.islower():
                    common_char_group_priority.append(string.ascii_lowercase.index(first_item) + 1)
            else:
                    common_char_group_priority.append(string.ascii_uppercase.index(first_item) + 27)
            count = count + 1
            break

print("Sum for the 3 groups part2 is:", sum(common_char_group_priority))


