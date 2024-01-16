#문자열 뒤집기
s = input()
bin = list(map(int, s))

result_zero=0
for i in range(len(bin)-1):
    if len(set(bin))==1:
        break
    if bin[i] == 0:
        bin[i]=1
        if bin[i+1] == 1:
            result_zero+=1

result_one=0
for i in range(len(bin)-1):
    if len(set(bin))==1:
        break
    if bin[i] == 1:
        bin[i]=0
        if bin[i+1] == 0:
            result_one+=1

    
print(min(result_zero, result_one))