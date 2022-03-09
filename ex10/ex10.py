txt = open('clown.txt')
di = dict()

for line in txt:
    line = line.rstrip()
    words = line.split()
    for w in words:
        di[w] = di.get(w,0) + 1

sortedList = list()
for k,v in di.items():
    tmpt = (v,k)
    sortedList.append(tmpt)

sortedList = sorted(sortedList[:5], reverse=True)

for v,k in sortedList:
    print(k,v)
