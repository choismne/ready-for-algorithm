def solution(s):
    stack = []
    for comp in s:
        if comp == '(':
            stack.append(comp)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False