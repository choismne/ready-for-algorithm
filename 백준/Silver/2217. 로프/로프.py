n = int(input())

li = []
max = -1

for _ in range(n):
    li.append(int(input()))
li.sort()

for i in range(n):
    if max < li[i]*(n-i):
        max = li[i]*(n-i)

print(max)