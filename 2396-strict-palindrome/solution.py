def isStrictlyPalindromic(n):
    base = 2
    result = True

    while (result and base < n-1):
        result = isPalindrome(toBase(n, base))
        base += 1

    return result


def isPalindrome(s):
    l = 0
    r = len(s) - 1

    while r > l:
        if s[l] != s[r]:
            return False
        r -= 1
        l += 1

    return True


def toBase(n, b):
    if n == 0:
        return '0'
    nums = []

    while n:
        n, r = divmod(n, b)
        nums.append(str(r))

    return ''.join(reversed(nums))


print(isStrictlyPalindromic(4))
