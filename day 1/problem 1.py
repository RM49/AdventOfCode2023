
textfile = open("data.txt", "r")
inp = textfile.readlines()
values = []
for s in inp:
    values.append(s.strip("\n"))

total = 0
for v in values:
    stringlist = list(v)
    integerlist = []
    for s in stringlist:
        try:
            int(s)
            integerlist.append(s)
        except ValueError:
            pass
    if len(integerlist) == 1:
        total += int(integerlist[0] + integerlist[0])
    else:
        num = int(integerlist[0] + integerlist[-1])
        total += num
print(total)

