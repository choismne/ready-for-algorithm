from itertools import permutations

def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    babyComb = []
    
    for i in range(1, 5):
        per = permutations(baby, i)
        for p in per:
            babyComb.append(''.join(p))
            
    cnt = 0
    for bab in babbling:
        if bab in babyComb:
            cnt+=1
        
    
    return cnt