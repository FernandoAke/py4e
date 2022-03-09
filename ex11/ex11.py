import re
hand = open('test.txt')

lookfor = input('Enter regex to look for: ')

for line in hand:
    line = line.rstrip()
    if re.search(lookfor, line):
        print(line)
