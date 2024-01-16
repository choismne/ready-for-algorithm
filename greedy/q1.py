n = int(input())
fear = list(map(int, input().split()))

count = 0
guild=[]
for f in fear:
    guild.append(f)
    if len(guild) == max(guild):
        count+=1
        print(guild)
        guild=[]
    

print(count)
