#볼링공 고르기 (2019 소마 기출)
n, m = input().split()
n = int(n)
m = int(m)

balls = list(map(int, input().split()))
test = []

count=0
for i in range(n):
    for j in range(i+1, n):
        if balls[i] != balls[j]:
            count+=1
            test.append((i+1, j+1))

print(count)
print(test)
