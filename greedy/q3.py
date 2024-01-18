#문자열 뒤집기
# s = input()
# bin_0 = list(map(int, s))
# bin_1 = list(map(int, s))

# result_zero=0
# for i in range(len(bin_0)-1):
#     if len(set(bin_0))==1:
#         break
#     if bin_0[i] == 0:
#         bin_0[i]=1
#         if bin_0[i+1] == 1:
#             result_zero+=1

# result_one=0
# for i in range(len(bin_1)-1):
#     if len(set(bin_1))==1:
#         break
#     if bin_1[i] == 1:
#         bin_1[i]=0
#         if bin_1[i+1] == 0:
#             result_one+=1

    
# print(min(result_zero, result_one))

s = input()
count_zero = 0
count_one = 0

if s[0] == '1':
    count_zero+=1
else:
    count_one+=1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count_zero+=1
        else:
            count_one+=1

print(min(count_zero, count_one))