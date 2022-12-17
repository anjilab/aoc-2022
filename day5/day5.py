moving_stack = []
with open('day5.txt') as f:
    sum = 0
    while True:
        line = f.readline()
        # test = f.read().splitlines()
        # print(test)
        if( 'move' in line):
            line_information = line.split(' ')
            count = line_information[1]
            from_stack = line_information[3]
            to_stack = line[5]
            current_stack = [line_information[1], line_information[3], line_information[5]]
            moving_stack.append(current_stack)
        if not line:
            break

# stacks = [["N", "Z"],["D", "C", "M"],["P"]]

stacks = [["D","T","W","N","L",], ["H", "P", "C"], 
["J","M", "G","D","N","H","P","W",], ["L","Q","T","N","S","W","C",], 
["N","C","H","P",],["B","Q","W","M","D","N","H","T"],
["L","S","G","J","R","B","M",],["T","R","B","V","G","W","N","Z",],
["L","P","N","D","G","W",]]
    
# PART 1
# for move_task in moving_stack:
#     number_of_element = move_task[0]
#     for num in range(0,int(number_of_element)):
#         stack_number_from = move_task[1]
#         stacks[int(move_task[2])-1].insert(0,stacks[int(move_task[1])-1][0])
#         stacks[int(move_task[1])-1].pop(0)

# PART 2
for move_task in moving_stack:
    number_of_element = move_task[0]
    test = []
    for num in range(0,int(number_of_element)):
        stack_number_from = move_task[1]
        # stacks[int(move_task[2])-1].insert(0,stacks[int(move_task[1])-1][0])
        inserted_str = stacks[int(move_task[1])-1][0]
        test.append(inserted_str)
        stacks[int(move_task[1])-1].pop(0)
    
    for item in reversed(test):
        stacks[int(move_task[2])-1].insert(0,item)
    
print(stacks)
    