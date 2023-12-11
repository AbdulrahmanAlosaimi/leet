def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return True
    if len(flowerbed) == 1 and flowerbed[0] == 0:
        flowerbed[0] = 1
        n -= 1
    else:
        for i in range(0, len(flowerbed)):
            if n == 0:
                break
            if flowerbed[i] == 1:
                continue
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    continue

                if i == (len(flowerbed) - 1) and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    continue

                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

    return n == 0


print(canPlaceFlowers([0], 0))
