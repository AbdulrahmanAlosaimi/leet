def generate(numRows):
    result = []
    for i in range(numRows):
        if (i == 0):
            result.append([1])
            continue
        else:
            addArr = [1]
            for j in range(1, len(result[-1])):
                #                if (j == 0) or (j == len(result) - 1):
                #                    addArr.append(1)
                #                    continue
                addArr.append((result[-1][j] + result[1][j-1]))
            addArr.append(1)
            result.append(addArr)
    return result


print(generate(5))
