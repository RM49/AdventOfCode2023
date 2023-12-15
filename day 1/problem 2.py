### 
### Attempt includes indexing substrings and indexing the integers then trying to find which one is last
###
textfile = open("data.txt", "r")
inp = textfile.readlines()
values = []
for s in inp:
    values.append(s.strip("\n"))

numwords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
for v in values:
    wordnums = []
    w = []
    
    for n in numwords:
        if n in v:
            wordnums.append(n)

            
    if len(wordnums) > 0:
        wordnumindexes = []
        for n in wordnums:
            wordnumindexes.append(v.index(n))
        w.append(wordnums[wordnumindexes.index(min(wordnumindexes))])
        
        # again, have to find the last word number by reversing the input and looking for the reverse of the number
        reversenumbers = []
        for n in numwords:
            reversenumbers.append(n[::-1])
        reversev = v[::-1]
        wordnumindexes = []
        
        for n in wordnums:
            wordnumindexes.append(reversev.index(n[::-1]))
        w.append(wordnums[wordnumindexes.index(min(wordnumindexes))])
        wordnums = w
    
    stringlist = list(v)
    integerlist = []
    for s in stringlist:
        try:
            int(s)
            integerlist.append(s)
        except ValueError:
            pass

    
    firstnum = 0
    if len(integerlist) < 1:
        firstnum = wordnums[0]
    elif len(wordnums) < 1:
        firstnum = integerlist[0]
    else:
        for n in wordnums:
            if v.index(n) < v.index(integerlist[0]):
                firstnum = n
                break # avoids changing firstnum to a letter num that is later but before the first int
        if firstnum == 0:
            firstnum = integerlist[0]

    #    indexing gives the first find, need to do in reverse to find the true last

    reverse = list(v)
    reverse.reverse()
    v2 = ""
    for r in reverse:
        v2 += r
    if len(wordnums) > 0:
        lastnumword = wordnums[-1][::-1]
    secondnum = 0
    if len(integerlist) < 1:
        secondnum = wordnums[-1]
    elif len(wordnums) < 1:
        secondnum = integerlist[-1]
    else:    
        
        if v2.index(lastnumword) < v2.index(integerlist[-1]):
            secondnum = wordnums[-1]
        if secondnum == 0:
            secondnum = integerlist[-1]
    #print(integerlist, firstnum, secondnum)
    num = []
    try:
        int(firstnum)
        num.append(firstnum)
    except ValueError:
        num.append(str(numwords.index(firstnum) + 1))

    try:
        int(secondnum)
        num.append(secondnum)
    except ValueError:
        num.append(str(numwords.index(secondnum) + 1))

    #print(v, firstnum, secondnum)
    number = num[0] + num[1]

    total += int(number)
    
print(total)

