def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    answer=0
    while A:
        pop_a = A.pop(0)
        pop_b = B.pop(0)
        answer += pop_a*pop_b

    return answer