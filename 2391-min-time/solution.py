def garbageCollection(garbage, travel):
    metalTime = paperTime = glassTime = 0
    mIndex = pIndex = gIndex = -1
    for i in range(len(garbage)):
        for j in range(len(garbage[i])):
            if garbage[i][j] == "M":
                if mIndex and mIndex != i and mIndex > -1:
                    for k in range(mIndex, i - 1):
                        metalTime += travel[k]
                metalTime += 1
                mIndex = i
            elif garbage[i][j] == "P":
                if pIndex and pIndex != i and pIndex > -1:
                    for k in range(pIndex, i - 1):
                        paperTime += travel[k]
                paperTime += 1
                pIndex = i
            else:
                if gIndex and gIndex != i and gIndex > -1:
                    for k in range(gIndex, i - 1):
                        glassTime += travel[k]
                glassTime += 1
                gIndex = i
        if i > 0:
            if "M" in "".join(garbage[i:]):
                metalTime += travel[i - 1]
            if "P" in "".join(garbage[i:]):
                paperTime += travel[i - 1]
            if "G" in "".join(garbage[i:]):
                glassTime += travel[i - 1]

    return metalTime + paperTime + glassTime


print(garbageCollection(["MMM", "PGM", "GP"], [3, 10]))
