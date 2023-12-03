import re

with open('example.txt', 'r') as input_file:
    data = input_file.read().split('\n')

games = []
for i in data:
    games.append(i.split(':'))

maximum = {'red': 12,
           'green': 13,
           'blue': 14}

powers = []
games_allowed = []
for i in games:
    status = True
    game = int(i[0].split(' ')[1])
    plays = re.findall("\d+\s\w+", i[1])
    hands = [j.split(' ') for j in plays]
    minimum = {'red': 0, 'green': 0, 'blue': 0}
    for k in hands:
        if int(k[0]) > minimum[k[1]]:
            minimum[k[1]] = int(k[0])
    
    minimum_list = list(minimum.values())
    power = 1
    for i in minimum_list:
        power = power*i
    powers.append(power)

print(sum(powers))
    