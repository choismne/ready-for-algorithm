def solution(wallpaper):
    index_list = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                index_list.append([i, j])
                
    index_list.sort()
    left = index_list[0][0]
    index_list.sort(key=lambda x : x[1])
    top = index_list[0][1]
    
    index_list.sort(reverse=True)
    right=index_list[0][0]
    index_list.sort(reverse=True, key=lambda x:x[1])
    bottom = index_list[0][1]
    
    return([left, top, right+1, bottom+1])
