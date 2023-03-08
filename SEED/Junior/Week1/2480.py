Dice = list(map(int,input().split()))
Dice.sort()
low, mid, high = Dice[0], Dice[1], Dice[2]


#풀이 1
if low == mid and mid == high:
    print(10000 + low * 1000)
if low == mid and low != high:
    print(1000 + low * 100)
if low == high and low != mid:
    print(1000 + low * 100)
if high == mid and high != low:
    print(1000 + high * 100)
if low != mid and mid != high:
    print(high * 100)

#풀이2
if high == mid :
    if mid == low :
        print(10000 + high * 1000)
    else :
        print(1000 + mid * 100)
else :
    if mid == low :
        print(1000 + mid * 100)
    else :
        print(high * 100)

#풀이3

# A, A, ?
if high == mid :
    # A, A, A
    if mid == low :
        case = 1
    # A, A, B
    else :
        case = 2
# A, B, ?
else :
    # A, B, B
    if mid == low :
        case = 2
    # A, B, C
    else :
        case = 3

# A, A, A
if case == 1 :
    print(10000 + high * 1000)
# A, A, B or A, B, B
elif case == 2 :
    print(1000 + mid * 100)
# A, B, C
else :
    print(high * 100)