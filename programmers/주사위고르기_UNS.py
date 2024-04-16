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
            
        for comb1 in product(set_1_dice[i].keys(), repeat = len(set_1)):     
            res_1 = {}
            for i in range(len(set_1)):
                tmp_1 += dice[set_1[i]-1][comb1[i]]
            for comb2 in product(range(len(set_1_dice[i])), repeat = len(set_2)):
                tmp_2 = 0
                for j in range(len(set_2)):
                    tmp_2 += dice[set_2[j]-1][comb2[j]]
                    
                if tmp_1 > tmp_2 : 
                    win_1 += 1
                elif tmp_2 > tmp_1 :
                    win_2 += 1
        
        if win_1 > MAX : 
            best = set_1
            MAX = win_1
        if win_2 > MAX : 
            best = set_2
            MAX = win_2
    
    return sorted(best)