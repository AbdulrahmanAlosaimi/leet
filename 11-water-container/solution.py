def maxArea(height):
    maxArea = 0

    lIndex = 0
    rIndex = len(height) - 1

    while lIndex <= rIndex:
        area = (min(height[lIndex], height[rIndex])) * (rIndex - lIndex)
        maxArea = max(maxArea, area)

        if height[lIndex] > height[rIndex]:
            rIndex -= 1
        else:
            lIndex += 1

    return maxArea


print(maxArea([1, 1]))
