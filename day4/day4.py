moving_stack = []
with open('day4.txt') as f:
    line = f.read().splitlines()
    pair = 0
    for val in line:
        groups =  val.split(',')
        group1 = groups[0]
        group2 = groups[1]
        group_range1 = group1.split('-')
        group_range2 = group2.split('-')

        range1 = list(range(int(group_range1[0]), int(group_range1[1])+1))
        range2 = list(range(int(group_range2[0]), int(group_range2[1])+1))

        if any([item in range1 for item in range2]):
            pair = pair + 1
        else:
            if any([item in range2 for item in range1]):
                pair = pair + 1
    print(f'Pairs are {pair}')



    
        
        

    