def knapsack(weights, values, capacity):
    # 메모이제이션을 위한 2차원 리스트 초기화
    DP = [[-1 for j in range(capacity+1)] for i in range(len(weights)+1)]

    # 재귀함수를 이용한 메모이제이션
    def recursive_knapsack(i, remain_capacity):
        # 저장된 결과가 있으면 반환
        if DP[i][remain_capacity] != -1:
            return DP[i][remain_capacity]

        # 더 이상 고를 아이템이 없거나 배낭 용량이 0이면 0 반환
        if i == 0 or remain_capacity == 0:
            return 0

        # i번째 아이템을 선택하지 않을 경우
        exc_tmp = recursive_knapsack(i-1, remain_capacity)

        # i번째 아이템을 선택할 경우
        inc_tmp = 0
        if remain_capacity >= weights[i-1]:
            inc_tmp = values[i-1] + recursive_knapsack(i-1, remain_capacity-weights[i-1])

        # 두 경우 중 더 큰 값을 저장하고 반환
        DP[i][remain_capacity] = max(exc_tmp, inc_tmp)
        return DP[i][remain_capacity]

    # 재귀함수 호출
    return recursive_knapsack(len(weights), capacity)
