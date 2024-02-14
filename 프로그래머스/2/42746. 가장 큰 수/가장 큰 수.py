def solution(numbers):
    answer = ''
    new_list = list(map(str, numbers))
    new_list.sort(key=lambda x:x*3, reverse=True)
    for comp in new_list:
        answer+=comp
    return str(int(answer))