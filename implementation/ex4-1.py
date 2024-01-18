n = int(input())

plans = input().split()
coordinate = [1, 1]
for plan in plans:
    if plan == 'L':
        if coordinate[1] != 1:
            coordinate[1] -= 1
    elif plan == 'R':
        if coordinate[1] != 5:
            coordinate[1] += 1
    elif plan == 'U':
        if coordinate[0] != 1:
            coordinate[0] -= 1
    elif plan == 'D':
        if coordinate[0] != 5:
            coordinate[0] += 1

print(coordinate[0], coordinate[1])

