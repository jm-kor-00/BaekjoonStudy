def findMedian_BruteForce1(nums1, nums2):
    #nums1과 nums2를 각각 완전탐색하기 위해 두 개의 키값 선언
    key1 = 0
    key2 = 0
    merged = []

    # 병합정렬에서의 부분 정렬이 끝난 후 병합하는 과정을 옮김 
    while key1 < len(nums1) and key2 < len(nums2):

        # 각각의 키값의 요소를 비교하며 작은 것을 merge배열에 넣으면서 진행
        if nums1[key1] < nums2[key2]:
            merged.append(nums1[key1])
            key1 += 1
        else :
            merged.append(nums2[key2])
            key2 += 1

    # nums1과 nums2중에 요소가 남아있는 배열을 merged 말단에 그대로 추가
    if key1 < len(nums1):
        merged += nums1[key1:]
    else :
        merged += nums2[key2:]
    
    # 짝수라면 (길이의 절반) 번째, (절반 + 1) 번째 숫자의 평균이 답
    if len(merged) % 2 == 0:
        return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
    # 홀수라면 (길이의 절반 + 1) 번째 숫자의 평균이 답
    else :
        return merged[len(merged) // 2]
    
def findMedian_Only1Array(nums1, nums2):
    mid = (len(nums1) + len(nums2)) // 2

    # 0. median 정의
    # 전체 크기가 홀수라면 nums1 + nums2 에서 mid + 1 번째 숫자가 median
    # 전체 크기가 짝수라면 nums1 + nums2 에서 mid 번째와 mid+1 번째 숫자의 평균이 median

    
    # 1. median을 구하기 위해선 mid+1 번째 숫자가 무엇인지 구해야 함
    
    # 2. merged array에서 mid + 1번째 보다 작은 수는 mid개임이 자명함

    # 3. 만약 nums1에 임의의 수 K 보다 작거나 같은 숫자가 A개 있다면
    #    nums2에는 K보다 작거나 같은 수가 mid - A개가 있음이 확실함

    # 반대로, nums2에서도 임의의 수 S 보다 작거나 같은 숫자가 A개 있다면
    # nums1에는 K보다 작거나 같은 수가 mid - A개가 있음이 확실함

    # 4. 따라서, 찾아야 하는 median은 
    
    # 전체 크기 홀수의 경우,
    # nums1[A + 1] or nums2[mid - A] : mid+1 번째 숫자 이다.
    
    # 전체 크기 짝수의 경우,
    # nums1[A + 1] or nums2[mid - A] : mid+1 번째 숫자
    # nums1[A] or nums2[mid - A - 1] : mid 번째 숫자 를 구해야 함

    # 5. mid는 전체길이 // 2 이므로 A만 구하면 median을 구할 수 있음
    # A를 0부터 1씩 증가시키며 적합한 A가 무엇인지 찾으면 됨

    key1 = 0 #key1은 주석에서의 A를 나타냄
 
    # key1을 0부터 증가시키며 완전탐색을 수행
    # nums1의 전체요소를 탐색할 수도 있으므로 O(N)의 시간복잡도    
    while key1 < len(nums1):
        print(key1)
        # 6. key1이 정확한 값인지 확인하는 방법은
        # 주석 3의 내용을 코드로 구현하면 됨
        
        # A가 정확한 위치라면
        # nums1[ 0 ~ A ]는 nums2[mid - A]보다 작거나 같아야 함
        # nums2[ 0 ~ mid-A-1 ]는 nums1[A + 1]보다 작거나 같아야 함

        if nums1[key1] <= nums2[mid - key1] and nums2[mid - key1 - 1] <= nums1[key1 + 1]:
            #현재 key1에서 nums1[:key1 + 1]와 nums2[:mid - key1]의 요소개수 합은 mid개를 만족함
            break
        key1 += 1
    
    # 7. 홀수 : nums1[A + 1] 와 nums2[mid - A] 중 median을 확정지어서 반환
    # 둘 중의 작은 값이 mid + 1번째 숫자임만은 자명함
    if (len(nums1) + len(nums2)) % 2 != 0:
        return min(nums1[key1 + 1], nums2[mid - key1])
    
    # 8. 짝수 : mid번째, mid+1번째 숫자의 평균이 median
    # nums1[A + 1] 와 nums2[mid - A] 중 작은 숫자 = mid+1 번째 숫자
    # nums1[A] or nums2[mid - A - 1] 중 큰 숫자 = mid 번째 숫자
    else :
        sumOfMids = max(nums1[key1],nums2[mid - key1 - 1]) + min(nums1[key1 + 1],nums2[mid - key1])
        return sumOfMids / 2
    
def findMedian_BinarySearch(nums1, nums2):
    mid = (len(nums1) + len(nums2)) // 2
    # 전체 크기가 홀수라면 nums1 + nums2 에서 mid + 1 번째 숫자가 median
    # 전체 크기가 짝수라면 nums1 + nums2 에서 mid번째와 mid+1 번째 숫자의 평균이 median

    # Only1Array에서는 nums1의 0부터 N번 인덱스 숫자까지를 탐색함 : O(N)
    # 탐색 종료 조건은 Only1Array와 동일하지만
    
    # 탐색방식을 이분탐색으로 개선하여
    # 탐색연산 횟수가 O(N)에서 O(logN) 으로 개선

    # 이분탐색 과정
    left = 0; right = len(nums1) - 1
    while left <= right :
        # key1 = left와 right의 mid
        # 완전탐색과 마찬가지로 key1(= A) 을 갱신하며 진행함
        key1 = (left + right) // 2

        if nums1[key1] > nums2[mid - key1] :
            #key1이 필요한 값 보다 큰 숫자이기 때문 -> key1이 작아져야 함
            # -> right를 갱신
            right = key1 - 1

        elif nums2[mid - key1 - 1] > nums1[key1 + 1] :
            #key1이 필요한 값 보다 작은 숫자이기 때문 -> key1이 커져야 함
            # -> left를 갱신
            left = key1 + 1

        else :
            #조건만족
            break
    if (nums1 + nums2) % 2 != 0:
        return min(nums1[key1 + 1], nums2[mid - key1])
    else :
        sumOfMids = max(nums1[key1],nums2[mid - key1 - 1]) + min(nums1[key1 + 1],nums2[mid - key1])
        return sumOfMids / 2
    


arr1 = []
arr2 = []
print(findMedian_BruteForce1([1,2],[3,4]))
print(findMedian_Only1Array([1,2],[3,4]))
print(findMedian_BinarySearch([1,2],[3,4]))