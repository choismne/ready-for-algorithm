position = list(input())
row, col = ord(position[0])-96, int(position[1])

# count = 0

# if col-2 > 0 and row-1 > 0: #왼쪽으로 두번, 위로 한번 가능한 경우
#     count+=1
# if col-2 > 0 and row+1 < 9: #왼쪽으로 두번, 아래로 한번 가능한 경우
#     count+=1
# if col+2 < 9 and row -1 > 0: #오른쪽으로 두번, 위로 한번 가능한 경우
#     count+=1
# if col+2 < 9 and row+ 1 < 9: #오른쪽으로 두번, 아래로 한번 가능한 경우
#     count+=1
# if row-2 > 0 and col-1 > 0: #위로 두번, 왼쪽로 한번 가능한 경우
#     count+=1
# if row-2 > 0 and col+1 < 9: #위로 두번, 오른쪽로 한번 가능한 경우
#     count+=1
# if row+2 < 9 and col -1 > 0: #아래로 두번, 왼쪽로 한번 가능한 경우
#     count+=1
# if row+2 < 9 and col+ 1 < 9: #아래로 두번, 오른쪽로 한번 가능한 경우
#     count+=1

# print(count)

#이렇게 가능한 경우에 대한 리스트를 만들어 놓고 하면 훨씬 더 간결하게 코드 작성가능
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

count = 0
for step in steps:
    next_row = row+step[0]
    next_col = col+step[1]
    if next_row >=1 and next_row <= 8 and next_col >=1 and next_col <= 8:
        count+=1

print(count)
     