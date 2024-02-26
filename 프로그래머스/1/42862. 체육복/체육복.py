def solution(n, lost, reserve):
    start = [1 for _ in range(n)]
    for res in reserve:
        start[res-1] += 1
    for lo in lost:
        start[lo-1] -= 1
        
    for i in range(n):
        if start[i] == 2:
            if i-1 >= 0 and start[i-1] == 0:
                start[i] -= 1
                start[i-1] += 1
            elif i+1 <= n-1 and start[i+1] == 0:
                start[i] -= 1
                start[i+1] += 1
    
    cnt=0
    for st in start:
        if st>0:
            cnt+=1
    
    return cnt