def findSpecialInteger(arr):
    specialInt = 0
    maxOcc = 0
    for i in range(len(arr)):
        if arr.count(arr[i]) > maxOcc:
            maxOcc = arr.count(arr[i])
            specialInt = arr[i]
        if (maxOcc > (len(arr) // 4) + 1):
            break
    return specialInt


print(findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
