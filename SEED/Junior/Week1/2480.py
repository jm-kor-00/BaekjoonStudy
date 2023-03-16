dice1, dice2, dice3 = map(int,input().split())

#셋 다 같은 경우
if dice1 == dice2 == dice3:
    print(10000 + dice1 * 1000)
#두 개가 같은 경우
elif dice1 == dice2:
    print(1000 + dice1 * 100)
elif dice1 == dice3:
    print(1000 + dice1 * 100)
elif dice2 == dice3:
    print(1000 + dice2 * 100)
#모두 다른 경우
else:
    print(100 * max(dice1,dice2,dice3))