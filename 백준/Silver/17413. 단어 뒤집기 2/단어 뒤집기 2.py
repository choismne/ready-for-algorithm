s = input()
check = True

stack = []

for comp in s:
    if comp == '<':
        while stack:
            print(stack.pop(), end='')
        print('<', end='')
        check = False
    elif comp == '>':
        while stack:
            print(stack.pop(0), end='')
        print('>', end='')
        check = True
    elif comp == ' ' and check:
        while stack:
            print(stack.pop(), end='')
        print(' ', end='')
    else:
        stack.append(comp)

if stack:
    while stack:
        print(stack.pop(), end='')




        
