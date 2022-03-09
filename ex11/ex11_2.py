import re
hand = open('test.txt')
total = 0
for line in hand:
    line = line.rstrip()
    if re.search('^New Revision: [0-9]+', line):
        x = re.findall('^New Revision: ([0-9]+)', line)
        total += int(x[0])

print(total)
