# PART1
X = 1
check_count = 20
sum_arr = []
with open('day10.txt') as f:
    instructions = f.read().splitlines()
    cycle = 0        
    for instruction in instructions:
        main_instruction = instruction.split(' ')
        if len(main_instruction) > 1:
            for i in range(2):
                cycle= cycle+1
                if cycle == check_count:
                    print('cycle', X, cycle)
                    sum_arr.append(X*cycle)
                    check_count = check_count + 40
                if i == 1:
                    X = X + int(main_instruction[1])
        else:
            cycle = cycle + 1
            if cycle == check_count:
                sum_arr.append(X*cycle)
                check_count = check_count + 40


print(sum(sum_arr))


