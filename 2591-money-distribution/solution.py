def distMoney(money, children):
    if children == money:
        return 0
    if money < 8 or children > money:
        return -1

    returnAmount = money % 8
    if returnAmount == 0:
        return children
    return returnAmount - children


print(distMoney(1, 3))
