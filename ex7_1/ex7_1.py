file = input("Enter the file name: ")

txt = open(file)

x = 0.0

for l in txt:
    ls = l.rstrip()
    print(ls)


    lookup = "X-DSPAM-Confidence: "
    if lookup in ls:
        for word in ls:
            try:

                x += int(word)
            except Exception as e:
                continue

print(x)
