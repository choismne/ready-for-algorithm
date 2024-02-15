import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    check = True
    
    while True:
        if len(scoville) == 1:
            if scoville[0]>=K:
                break
            else:
                check=False
                break
        if all(x>=K for x in scoville):
            break
            
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new = a + b*2
        heapq.heappush(scoville, new)
        count += 1
        
    
    if check:
        return count
    else:
        return -1