def solution(id_list, report, k):
    len_id = len(id_list)
    report = list(set(report))
    answer = [0]*len_id
    li = [[] for _ in range(len_id)]
    cnt = [0 for _ in range(len_id)]

    for rep in report:
        do, get = rep.split()
        do_idx = id_list.index(do)
        li[do_idx].append(get)

        get_idx = id_list.index(get)
        cnt[get_idx] += 1

    for i in range(len_id):
        if cnt[i] >= k:
            for j in range(len_id):
                if id_list[i] in li[j]:
                    answer[j] += 1
                    
    return answer
