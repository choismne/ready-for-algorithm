inp = input()
stack = []
global_count = 0

for i in range(len(inp)):
    if inp[i] == '(':
        stack.append(['(', 1])
    else:
        if stack[-1][1] == 1:
            stack.pop()
            for st in stack:
                st[1] += 1
        else:
            global_count += stack.pop()[1]

print(global_count)