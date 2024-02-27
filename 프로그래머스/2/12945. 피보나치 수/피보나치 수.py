def solution(n):
    dp_table = [0]*n
    
    dp_table[0] = 1
    dp_table[1] = 1
    
    for i in range(2, n):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]
        
    return dp_table[n-1]%1234567
    