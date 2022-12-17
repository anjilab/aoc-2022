# PART1
with open('day7.txt') as f:
    commands = f.read().splitlines()
    for index, command in enumerate(commands):
        if '/' in command:
            print('root', index)
        if 'dir' in command:
            print(index)
            print(command)
    


