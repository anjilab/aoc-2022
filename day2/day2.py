from functools import reduce
strategy_guide = { 'A' : {type: 'rock' , "value": 1}, 'B' : {type: 'paper', "value": 2}, 'C' :{type: 'scissor', "value": 3} , 'X' : {type: 'rock' , "value": 1, "role" : 'lose'} , 'Y' :{type: 'paper', "value": 2, "role" : "draw"} , 'Z' : {type: 'scissor', "value": 3 , "role" : "win"}}
# Part 1
def check_win_or_loss_or_draw(opponent_shape, your_shape):
    priority = {'rock' : 'paper', 'paper' :'scissor' ,'scissor' :'rock'}
    if strategy_guide[opponent_shape][type] == strategy_guide[your_shape][type]:
        strategy_guide[your_shape]["value"] + 3
        return strategy_guide[your_shape]["value"] + 3
    if priority[strategy_guide[opponent_shape][type]] == strategy_guide[your_shape][type]:
        strategy_guide[your_shape]["value"] + 6
        return strategy_guide[your_shape]["value"] + 6
    else:
        strategy_guide[your_shape]["value"] 
        return strategy_guide[your_shape]["value"]

# Part 2
def check_win_or_loss_or_draw_part2(opponent_shape, your_shape):
    priority = {'rock' : 'paper', 'paper' :'scissor' ,'scissor' :'rock'}
    condition_output = {'win' : {'A' : 'Y' , 'B' : 'Z' , 'C' : 'X'},
    'lose' : {'A' : 'Z' , 'B' : 'X' , 'C' : 'Y'}}
    your_new_shape =  ''
    if strategy_guide[your_shape]["role"] == 'draw':
        your_new_shape = opponent_shape
    if strategy_guide[your_shape]["role"] == 'lose':
        your_new_shape= condition_output['lose'][opponent_shape]
    if strategy_guide[your_shape]["role"] == 'win':
        your_new_shape= condition_output['win'][opponent_shape]

    if strategy_guide[opponent_shape][type] == strategy_guide[your_new_shape][type]:
        strategy_guide[your_new_shape]["value"] + 3
        return strategy_guide[your_new_shape]["value"] + 3
    if priority[strategy_guide[opponent_shape][type]] == strategy_guide[your_new_shape][type]:
        strategy_guide[your_new_shape]["value"] + 6
        return strategy_guide[your_new_shape]["value"] + 6
    else:
        strategy_guide[your_new_shape]["value"] 
        return strategy_guide[your_new_shape]["value"]


def findSumOfEachRound(part):
    sum = []
    with open('day2.txt') as f:
        while True:
            line = f.readline()
            scores = line.split(" ")
            if(len(scores) > 0 and scores[0] != ''):
                if '\n' in scores[1]:
                    if part == '1':
                        score =  check_win_or_loss_or_draw(scores[0], scores[1].strip())   
                    else:
                        score = check_win_or_loss_or_draw_part2(scores[0], scores[1].strip())                    
                    sum.append(score)
                else:
                    if part == '1':
                        score = check_win_or_loss_or_draw(scores[0], scores[1])
                    else: 
                        score = check_win_or_loss_or_draw_part2(scores[0], scores[1])                        
                    sum.append(score)
            if not line:
                break
    return sum


part1 = findSumOfEachRound('1')
part2 = findSumOfEachRound('2')
print(reduce(lambda acc,x: acc+x, part1))
print(reduce(lambda acc,x: acc+x, part2))

