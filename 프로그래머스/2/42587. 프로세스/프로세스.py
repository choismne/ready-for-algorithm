def solution(priorities, location):
    prior = [(pr, idx) for idx, pr in enumerate(priorities)]
    
    count=0
    while prior:
        if prior[0][0] < max(prior)[0]:
            comp = prior.pop(0)
            prior.append(comp)
        else:
            count+=1
            comp = prior.pop(0)
            if comp[1] == location:
                return count
    