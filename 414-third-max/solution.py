def thirdMax(nums):
    sortedNums = list(sorted(set(nums)))
    if len(sortedNums) < 3:
        return sortedNums[-1]

    return sortedNums[-3]


print(thirdMax([2, 2, 3, 1]))
