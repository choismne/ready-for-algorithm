def solution(array, commands):
    answer = []
    for com in commands:
        new_list = array[com[0]-1:com[1]]
        new_list.sort()
        answer.append(new_list[com[2]-1])
    return answer