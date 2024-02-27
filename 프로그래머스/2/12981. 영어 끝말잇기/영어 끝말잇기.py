def solution(n, words):
    front = [words[0]]
    back = words[1:]
    
    while back:
        if front[-1][-1] != back[0][0]:
            return [len(front)%n+1, len(front)//n+1]
        elif back[0] in front:
            return [len(front)%n+1, len(front)//n+1]
        else:
            front.append(back.pop(0))
    
    return [0, 0]
        
        