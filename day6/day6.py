# PART1

with open('day6.txt') as f:
    input_signal = f.read()
    # input_signal = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    check_marker = ''
    count = 4
    for index,item in enumerate(input_signal):
        test_marker = input_signal[index:count]
        if len(test_marker) == len(list(set(test_marker))):
            break
        count = count + 1
    print(f'After 4 distinct char{count}')


# PART2
with open('day6.txt') as f:
    input_signal = f.read()
    check_marker = ''
    count = 14
    for index,item in enumerate(input_signal):
        test_marker = input_signal[index:count]
        if len(test_marker) == len(list(set(test_marker))):
            break
        count = count + 1
    print(f'After 14 distinct char{count}')


            

