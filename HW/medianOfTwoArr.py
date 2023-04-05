class Solution(object):
    # trial1
    def findMedian_BruteForce(self, nums1, nums2):
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
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2.0
        
        # 홀수라면 (길이의 절반 + 1) 번째 숫자의 평균이 답
        else :
            return merged[len(merged) // 2]
    #trial2
    def findMedian_SearchShortArray(self, nums1, nums2):
        # 길이가 짧은 배열은 arr1
        # 긴 배열을 arr2 라고 지정
        arr1 = nums1
        arr2 = nums2
        # len1은 arr1의 길이, len2는 arr2의 길이
        len1 = len(arr1)
        len2 = len(arr2)
        
        mid = (len1 + len2) // 2

        if len2 < len1 :
            arr2, arr1 = arr1, arr2

        # 0. median 정의
        # 전체 크기가 홀수라면 arr1 + arr2 에서 mid + 1 번째 숫자가 median
        # 전체 크기가 짝수라면 arr1 + arr2 에서 mid 번째와 mid+1 번째 숫자의 평균이 median

        # 1. median을 구하기 위해선 mid+1 번째 숫자가 어느쪽 배열에 있는지, 몇 번 인덱스인지 구해야 함

        # 2. merged array에서 mid + 1번째 보다 작거나 같은 요소는 mid 개 있는 것이 자명함

        # 3. 만약 어떤 임의의 수 K가 mid + 1 번째 요소가 맞다면,
        # nums1에 임의의 수 K 보다 작거나 같은 숫자가 A개 있고
        # arr2에는 K보다 작거나 같은 수가 mid - A개가 있음이 확실함

        # 반대로, arr2에서도 K 보다 작거나 같은 숫자가 A개 있다면
        # nums1에는 K보다 작거나 같은 수가 mid - A개가 있음이 확실함

        # 4. 따라서, 찾아야 하는 median을 다음과 같이 정의할 수 있음.

        # 전체 크기 홀수의 경우,
        # arr1[A + 1] or arr2[mid - A - 1] : 둘 중에 작은 것이 mid+1 번째 숫자 이다.

        # 전체 크기 짝수의 경우,
        # arr1[A + 1] or arr2[mid - A - 1] : 둘 중에 작은 것이 mid + 1 번째 숫자
        # arr1[A] or arr2[mid - A - 2] : 둘 중에 큰 것이 mid 번째 숫자

        # 5. mid는 전체길이 // 2 이므로 A만 구하면 median을 구할 수 있음
        # A를 1씩 증가시키며 적합한 A가 무엇인지 찾으면 됨

        key = -1 #key1은 주석에서의 A를 나타냄

        # key1을 1씩 증가시키며 완전탐색을 수행
        # nums1의 전체요소를 탐색할 수도 있으므로 O(N)의 시간복잡도
        while key < len(arr1):
            # 6. key1이 정확한 값인지 확인하는 방법은
            # 주석 3의 내용을 코드로 구현하면 됨

            # A가 정확한 위치라면
            # arr1[ 0 ~ A ]는 arr2[mid - A]보다 작거나 같아야 함
            # arr2[ 0 ~ mid-A-1 ]는 arr1[A + 1]보다 작거나 같아야 함

            # 인덱스로 인해 발생하는 오류를 방지
            # 인덱스 범위를 벗어나는 경우, 입력 가능한 최대(최소)값으로 수정
            # 비교 과정 에서 더 작은(더 큰) 숫자는 제거되므로 문제없음

            if (key) >= 0:
                left_1 = arr1[key]
            else : left_1 = -(10**6)    

            if (key + 1) >= len(arr1):
                right_1 = 10**6
            else : right_1 = arr1[key+1]

            if (mid - key - 2) >= 0:
                left_2 = arr2[mid - key - 2]
            else : left_2 = -(10**6)
            
            if (mid - key - 1) >= len(arr2):
                right_2 = (10**6)
            else : right_2 = arr2[mid - key - 1]
            
            # print(key,"에서",left_1,right_1,left_2,right_2)
            #조건만족 시,
            if left_1 <= right_2 and left_2 <= right_1 :
                break
            else : key += 1

        # 7. 홀수 : arr1[A + 1] 와 arr2[mid - A - 1] 중 median을 확정지어서 반환
        # 둘 중의 작은 값이 mid + 1번째 숫자임만은 자명함
        if (len(arr1) + len(arr2)) % 2 != 0:
            return min(right_1,right_2)

        # 8. 짝수 : mid번째, mid+1번째 숫자의 평균이 median
        # arr1[A] or arr2[mid - A - 2] 중 작은 숫자 = mid 번째 숫자
        # arr1[A + 1] 와 arr2[mid - A - 1] 중 큰 숫자 = mid+1 번째 숫자
        else :
            sumOfMids = max(left_1,left_2) + min(right_1,right_2)
            return sumOfMids / (2.0)
    #trial3
    def findMedian_BinarySearchForShortArray(self, nums1, nums2):
        arr1 = nums1
        arr2 = nums2
        len1 = len(arr1)
        len2 = len(arr2)
        
        mid = (len1 + len2) // 2

        if len2 < len1 :
            arr2, arr1 = arr1, arr2
        
        # Only1Array에서는 nums1의 -1 부터 N번 인덱스 숫자까지를 탐색함 : O(N)
        # 탐색 종료 조건은 trial2 와 동일하지만

        # 탐색방식을 이분탐색으로 개선하여
        # 탐색연산 횟수가 O(N)에서 O(logN) 으로 개선
        
        start = 0; end = len(arr1) - 1
        
        # 일방적인 이분탐색에서는 범위를 벗어나지 않게 하기 위해서
        # left <= right 를 조건으로 하지만
        # 이 방식은 left가 음수가 되거나 right가 범위보다 커지는 경우가 답일 수도 있기 때문에
        # 별도의 반복문 조건을 두지 않음
        while True:
            key = (start + end) // 2
            if (key) >= 0:
                left_1 = arr1[key]
            else : left_1 = -(10**6)    

            if (key + 1) >= len(arr1):
                right_1 = 10**6
            else : right_1 = arr1[key+1]

            if (mid - key - 2) >= 0:
                left_2 = arr2[mid - key - 2]
            else : left_2 = -(10**6)
            
            if (mid - key - 1) >= len(arr2):
                right_2 = (10**6)
            else : right_2 = arr2[mid - key - 1]


            if left_1 > right_2 :
                #key1이 필요한 값 보다 큰 숫자이기 때문 -> key1이 작아져야 함
                # -> right를 갱신
                end = key - 1
            elif left_2 > right_1:
                #key1이 필요한 값 보다 작은 숫자이기 때문 -> key1이 커져야 함
                # -> end를 갱신
                start = key + 1
            else :
                #조건만족 시
                break

        if (len1 + len2) % 2 != 0:
            return min(right_1,right_2)
            
        else :
            sumOfMids = max(left_1,left_2) + min(right_1,right_2)
            return sumOfMids / 2.0

S = Solution()
A = [1,2,3,4,5]
B = []
print("Arrays :",A,",",B)
print("Trial1 median :",S.findMedian_BruteForce(A,B))
print("Trial2 median :",S.findMedian_SearchShortArray(A,B))
print("Trial3 median :",S.findMedian_BinarySearchForShortArray(A,B))