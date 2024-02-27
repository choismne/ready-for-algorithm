from collections import deque

def solution(s):
    front = deque([])
    back = deque(list(s))
    while back:
        if len(front) == 0:
            front.append(back.popleft())
        elif front[-1] == back[0]:
            front.pop()
            back.popleft()
        else:
            front.append(back.popleft())
    
    if front:
        return 0
    else:
        return 1
            