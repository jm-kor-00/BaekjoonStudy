from itertools import combinations, product

def solution(dice):
    sets = list(combinations([x + 1 for x in range(len(dice))],len(dice)//2))
    MAX = 0

    for i in range(len(sets)):
        set_1 = list(sets[i])
        set_2 = list(sets[-1-i])
        win_1 = 0;win_2 = 0
        
        set_1_dice = []
        for dn in set_1:
            tmp = {}
            for i in range(6):
                if dice[dn-1][i] in tmp :
                    tmp[dice[dn-1][i]] += 1
                else :
                    tmp[dice[dn-1][i]] = 1
                    
            set_1_dice.append(tmp)
        
        set_2_dice = []
        for dn in set_2:
            tmp = {}
            for i in range(6):
                if dice[dn-1][i] in tmp :
                    tmp[dice[dn-1][i]] += 1
                else :
                    tmp[dice[dn-1][i]] = 1   
            set_2_dice.append(tmp)
        
        res_1 = {}
        for dic in set_1_dice:
            for point in dic.keys():
                point
            
        
        if win_1 > MAX : 
            best = set_1
            MAX = win_1
        if win_2 > MAX : 
            best = set_2
            MAX = win_2
    
    return sorted(best)