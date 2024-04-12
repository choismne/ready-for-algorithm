t = int(input())


for _ in range(t):
    n = int(input())
    q = n//25
    n = n%25

    d = n//10
    n = n%10

    nc = n//5
    n = n%5

    p = n//1
    print(q, d, nc, p)

    

