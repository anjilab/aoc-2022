moving_stack = []
with open('day21.txt') as f:
    line = f.read().splitlines()
    dict_of_monkey ={}
    for val in line:
        monkey_task_split = val.split(':')
        monkey_name = monkey_task_split[0]
        monkey_task_or_number = monkey_task_split[1].strip()
        if monkey_task_or_number.isdigit():
            dict_of_monkey[monkey_name] = int(monkey_task_or_number)
        else:
            dict_of_monkey[monkey_name] = monkey_task_or_number


def findMyVal(monkey_name):
    prepareDict = {}
    str = dict_of_monkey[monkey_name]
    operators = ['+', '-', '/', '*']
    if not isinstance(str,int):
        operator = [item for item in str if item in operators][0]
        if operator:
            after_split = str.split(operator)
            number_1 =after_split[0].strip()
            number_2 =after_split[1].strip()
            print(operator, number_1,number_2)
            calculate = findMyVal(number_1)
                  
        else:
            prepareDict({monkey_name: str})
            print('heere')
    else:
        operand1 = dict_of_monkey[monkey_name]
        print(monkey_name, operand1)

    print(prepareDict)
        
# for x in dict_of_monkey:

findMyVal('root')
    # number_yelled = 0
    # if x == 'root' and isinstance(dict_of_monkey['root'], int):
    #     print(dict_of_monkey['root'])        
    # else:
    #     if x !=  'root': 
    #         print('here', findMyVal(x))
    #     else:
    #         print('====', findMyVal(x))
            
       
