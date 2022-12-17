# PART1
import string

dict = []






with open('day16.txt') as f:
    valve = f.read().splitlines()
    count = 1
    def get_corresponding():
        print('Get corresponding')
        for val in valve:
            split_valve = val.split(' ')
            valve_type = split_valve[1]
            valve_flow_rate = split_valve[4]
            valve_to = []
            for to_valve in range(9, len(split_valve)):
                valve_to.append(split_valve[to_valve])
            dict.append({"type": valve_type, "rate": valve_flow_rate.split('=')[1].replace(';', ''), "to": valve_to})

    print(get_corresponding())
    print(dict[0]['type'])
    def getFrom(from_type):
        print(from_type)
        return dict


    for item in range(30):
        count = 0
        from_valve = getFrom(item)
        print(from_valve)
        count +=1
            




