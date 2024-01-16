#곱하기 혹은 더하기
n = input()
nums = list(map(int, n))

result = nums[0]
for num in nums[1:]:
    if result*num >= result+num:
        result = result*num
    else:
        result = result+num

print(result)


