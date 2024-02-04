from random import randint

def roll(d):
    return randint(1,d)

def mod(stat):
    ret = -5
    for i in range(1,30,2):
        if stat <= i: return ret
        ret+=1
    return ret

backpacks={
    'Normal':4,
    'Survival':6
}