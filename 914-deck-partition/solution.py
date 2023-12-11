def hasGroupsSizeX(deck):
    for i in range(len(deck)):
        if deck.count(deck[i]) % 2 != 0:
            return False

    return True


print(hasGroupsSizeX([0,0,0,1,1,1,2,2,2]))
