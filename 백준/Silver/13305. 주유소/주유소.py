#백준 s3, 그리디, 13305 주유소
n = int(input())
oil = list(map(int, input().split()))
cost = list(map(int, input().split()))
oil.append(0)

stop=0
total = 0
for i in range(n-1):
    if cost[i] >= cost[i+1]:
        total += cost[stop]*oil[i]
        stop += 1
    else:
        total += cost[stop]*oil[i]

print(total)