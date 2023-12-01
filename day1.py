with open('example.txt', 'r') as input_file:
    data = input_file.read().split('\n')

print(data)
for i in data:
    number = ''
    for j in i:
        if j.isnumeric():
            number += j
            break
    for j in i[::-1]:
        if j.isnumeric():
            number += j
            break
    print(number)