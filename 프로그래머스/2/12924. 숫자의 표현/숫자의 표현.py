def solution(n):
    sequence = []
    for i in range(1, n+1):
        sequence.append(i)
    
    sum, left, count = 0, 0, 0
    
    for right in range(n):
        sum += sequence[right]
        while sum>n:
            sum -= sequence[left]
            left += 1
        if sum == n:
            count += 1
            
    return count