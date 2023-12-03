import re

with open('example.txt', 'r') as input_file:
    data = input_file.read().split('\n')

games = []
for i in data:
    games.append(i.split(':'))

maximum = {'red': 12,
           'green': 13,
           'blue': 14}

games_allowed = []
for i in games:
    status = True
    game = int(i[0].split(' ')[1])
    plays = re.findall("\d+\s\w+", i[1])
    hands = [j.split(' ') for j in plays]
    for k in hands:
        if int(k[0]) > maximum[k[1]]:
            status = False
    if status == True:
        games_allowed.append(game)

print(sum(games_allowed))
