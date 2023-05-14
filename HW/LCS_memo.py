def lcs_memo(s1, s2, i, j, memo):
    #메모지에이션으로 중복 계산 방지
    if memo[i][j] != -1:
        return memo[i][j]
    #한 쪽 문자열이 끝까지 탐색된 경우
    if i == 0 or j == 0:
        memo[i][j] = 0
    # 두 문자열의 마지막 문자가 같은 경우
    elif s1[i-1] == s2[j-1]:
        memo[i][j] = lcs_memo(s1, s2, i-1, j-1, memo) + 1
    # 두 문자열의 마지막 문자가 다른 경우
    else:
        memo[i][j] = max(lcs_memo(s1, s2, i, j-1, memo), lcs_memo(s1, s2, i-1, j, memo))

    return memo[i][j]