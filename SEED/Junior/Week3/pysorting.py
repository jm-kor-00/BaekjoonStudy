arr = [3,1,6,4,9,7,8,5,2]

#.sort 오름차순
arr.sort()

# 내림차순 = 큰 거부터
arr.sort(reverse=True)

print(arr)
# 문자열에 대해선?
brr = ["go","hello","seed","bye"]

#사전순으로 정렬됨
brr.sort()
#key를 지정 : 문자열 길이
brr.sort(key=lambda x : len(x))

print(brr)

# key 활용 2, 튜플
student = [("최나연",163),("은재민",183),("김민석",173),("김민석",180)]
# 이름순으로 정렬
# student.sort(key=lambda s: s[0])
# 키(height)순으로 정렬
student.sort(key=lambda s: s[1])
# 이름순으로 정렬한 후, 키를 큰 순으로 정렬하려면?
student.sort(key=lambda s: (s[0],-s[1])) #내림차순에선 -1을 곱해주는게 포인트!
print(student)