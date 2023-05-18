mush = [int(input()) for _ in range(10)]
score = 0

for tmp in mush:
    score += tmp
    if score >= 100:
        if score - 100 > 100 - (score-tmp):
            score -= tmp
        break
print(score)