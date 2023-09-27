def bound(obj,W,level,weight,profit):
    if weight > W :
        return 0
    
    pBound = profit
    for j in range(level+1,len(obj)):
        pBound += obj[j][1]
    
    return pBound

def bound2(arr,W,level,weight,profit):
    if weight > W:
        return 0
    
    pBound = profit
    tWeight = weight

    j = level + 1
    n = len(arr)
    while j < n and (tWeight+arr[j][0] <= W):
        tWeight += arr[j][0]
        pBound += arr[j][1]
        j += 1
    
    if j < n :
        pBound += (W - tWeight) * (arr[j][1]/arr[j][0])

    return pBound

def knapSack_bnb(obj,W,level,weight,profit,maxProfit):
    if (level == len(obj)):
        return maxProfit
    
    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        
        if newProfit > maxProfit:
            maxProfit = newProfit
        
        newBound = bound(obj,W,level,newWeight,newProfit)
        if newBound >= maxProfit:
            maxProfit = knapSack_bnb(obj,W,level+1,newWeight,newProfit,maxProfit)
        
    newWeight = weight
    newProfit = profit
    newBound = bound(obj,W,level,newWeight,newProfit)
    if newBound >= maxProfit :
        maxProfit = knapSack_bnb(obj,W,level+1,newWeight,newProfit,maxProfit)
    
    return maxProfit

def knapSack_bnb2(obj,W,level,weight,profit,maxProfit):
    if (level == len(obj)):
        return maxProfit
    
    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        
        if newProfit > maxProfit:
            maxProfit = newProfit
        
        newBound = bound2(obj,W,level,newWeight,newProfit)
        if newBound >= maxProfit:
            maxProfit = knapSack_bnb(obj,W,level+1,newWeight,newProfit,maxProfit)
        
    newWeight = weight
    newProfit = profit
    newBound = bound2(obj,W,level,newWeight,newProfit)
    if newBound >= maxProfit :
        maxProfit = knapSack_bnb(obj,W,level+1,newWeight,newProfit,maxProfit)
    
    return maxProfit
print("##############################################\n방법1:\n")
obj = [(2,20,"A"),(2.2,30,"B"),(1.5,60,"C"),(2,30,"D"),(5.1,10,"E")]
print(obj)
print("0-1배낭문제(분기한정): ",knapSack_bnb(obj,10,0,0,0,0))

obj.sort(key=lambda e : e[1]/e[0], reverse=True)
print("##############################################\n방법2:\n")
print(obj)
print("0-1배낭문제(분기한정): ",knapSack_bnb2(obj,10,0,0,0,0))