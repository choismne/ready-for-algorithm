def solution(friends, gifts):
    fl = len(friends)

    li = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    gift_index = [[0, 0, 0] for _ in range(len(friends))]

    for gift in gifts:
        give, get = map(str, gift.split())
        giv_idx = friends.index(give)
        get_idx = friends.index(get)
        gift_index[giv_idx][0] += 1
        gift_index[get_idx][1] += 1
        li[giv_idx][get_idx] += 1

    for i in range(len(gift_index)):
        gift_index[i][2] = gift_index[i][0]-gift_index[i][1]

    next_month = [0 for _ in range(fl)]

    for i in range(fl):
        for j in range(fl):
            if i!=j:
                if li[i][j] == 0 and li[j][i] == 0:
                    if gift_index[i][2] > gift_index[j][2]:
                            next_month[i] += 1
                    elif gift_index[i][2] < gift_index[j][2]:
                        next_month[j] += 1
                else:
                    if li[i][j] > li[j][i]:
                        next_month[i] += 1
                    elif li[i][j] < li[j][i]:
                        next_month[j] += 1
                    else:
                        if gift_index[i][2] > gift_index[j][2]:
                            next_month[i] += 1
                        elif gift_index[i][2] < gift_index[j][2]:
                            next_month[j] += 1

    for i in range(fl):
        next_month[i] = next_month[i]//2
        
    return max(next_month)




    
            
            
            
            
    