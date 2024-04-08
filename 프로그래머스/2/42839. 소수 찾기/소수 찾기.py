import math
from itertools import permutations

def generate_numbers(lst):
    numbers = []
    for i in range(1, len(lst) + 1):
        perms = permutations(lst, i)
        for perm in perms:
            number = int(''.join(map(str, perm)))
            if number not in numbers:
                numbers.append(number)
    return numbers

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    gen_numbers = generate_numbers(list(numbers))
    for num in gen_numbers:
        if is_prime(num):
            answer += 1
    return answer