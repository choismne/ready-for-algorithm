def solution(bandage, health, attacks):
    seq = 0
    now_health = health
    attack_times = [i[0] for i in attacks]
    for i in range(attacks[-1][0]+1):
        if i in attack_times:
            idx = attack_times.index(i)
            now_health -= attacks[idx][1]
            seq = 0
            if now_health <= 0:
                now_health = -1
                break
        else:
            now_health += bandage[1]
            if now_health > health:
                now_health = health
            seq += 1
            if seq == bandage[0]:
                now_health += bandage[2]
                seq=0
                if now_health > health:
                    now_health = health
                
    return now_health
      