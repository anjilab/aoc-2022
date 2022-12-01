f = open("day1-input.txt", "r")
# for x in f:
#     print(x)
sum_of_calories = []

with open('day1-input.txt') as f:
    sum = 0
    while True:
        line = f.readline()
        if line != '\n' and len(line) != 0:
            sum = sum + int(line)
        if line == '\n':
            sum_of_calories.append(sum)
            sum = 0
        if not line:
            break
        # print(line.strip())

print('Max calories is:', max(sum_of_calories))

# PART 2
sorted_list_calories = []
def get_sorted_list(list_of_calories):
    sorted_list_calories = [] + list_of_calories
    sorted_list_calories.sort(reverse = True)
    return sorted_list_calories

# print('Original calories:', sum_of_calories);
sorted_list_calories = get_sorted_list(sum_of_calories)
def get_total_top_3_calories():
    return sorted_list_calories[0] + sorted_list_calories[1] + sorted_list_calories[2]

print('Top total 3 calories sum is: ', get_total_top_3_calories())



