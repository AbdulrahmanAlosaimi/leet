def solution(s):
    
    stack = []
    rightChar = '])}'
    leftChar = '[{('
    
    if len(s) == 1 or s[0] in rightChar:
            return False
        
    for c in s:
        if c in leftChar:
            stack.append(c)
        elif c in rightChar:
            if len(stack) == 0:
                return False
            if c == '}' and stack[len(stack)-1] == '{':
                stack.pop()
            elif c == ']' and stack[len(stack)-1] == '[':
                    stack.pop()
            elif c == ')' and stack[len(stack)-1] == '(':
                    stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
        
    return False

        