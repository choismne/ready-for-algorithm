n = int(input())
inp = list(map(int, input().split()))
answer = [-1]*n
stack = [0]

for i in range(n):
    while stack and inp[stack[-1]] < inp[i]:
        idx = stack.pop()
        answer[idx] = inp[i]
    stack.append(i)

print(*answer)

