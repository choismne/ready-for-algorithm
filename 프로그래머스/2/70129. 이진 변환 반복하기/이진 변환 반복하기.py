def solution(s):
    global count_zero
    count_zero=0

    def delete_zero():
        new_s = ""
        global count_zero
        for comp in s:
            if comp == '1':
                new_s+=comp
            else:
                count_zero += 1
        return new_s

    def to_binary(s):
        l = len(s)
        return format(l, 'b')

    cnt=0
    while True:
        s = to_binary(delete_zero())
        cnt+=1
        if s=='1':
            break

    return [cnt, count_zero]