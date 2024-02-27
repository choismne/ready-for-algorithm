from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
q = deque()

for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if ' ' in cmd:
        cmd, num = cmd.split()
        num = int(num)
    length = len(q)

    if cmd == 'push_front':
        q.appendleft(num)
    elif cmd == 'push_back':
        q.append(num)
    elif cmd == 'pop_front':
        if length>=1:
            v = q.popleft()
            print(v)
        else:
            print(-1)
    elif cmd == 'pop_back':
        if length>=1:
            v = q.pop()
            print(v)
        else:
            print(-1)
    elif cmd == 'size':
        print(length)
    elif cmd == 'empty':
        if length == 0:
            print(1)
        else:
            print(0)
    elif cmd =='front':
        if length>=1:
            print(q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if length>=1:
            print(q[length-1])
        else:
            print(-1)


