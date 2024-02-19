def solution(n):
    bin_n = format(n, 'b')
    answer = n
    while True:
        answer += 1
        if bin_n.count('1') == format(answer, 'b').count('1'):
            break
    return answer