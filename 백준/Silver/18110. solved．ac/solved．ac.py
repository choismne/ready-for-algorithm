n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))
scores.sort()

def round2(a):
    return int(a) + (1 if a - int(a) >= 0.5 else 0)

if n==0:
    print(0)
else:
    sum=0
    p = round2(n*0.15)
    for i in range(p, n-p):
        sum += scores[i]

    print(round2(sum/(n-2*p)))