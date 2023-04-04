def findMedianSortedArrays(nums1, nums2):
    key1 = 0
    key2 = 0
    merged = []

    while key1 < len(nums1) and key2 < len(nums2):
        if nums1[key1] < nums2[key2]:
            merged.append(nums1[key1])
            key1 += 1
        else :
            merged.append(nums2[key2])
            key2 += 1

    if key1 < len(nums1):
        merged += nums1[key1:]
    else :
        merged += nums2[key2:]
    
    print(merged)
    if len(merged) % 2 == 0:
        return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
    else :
        return merged[len(merged) // 2]
    
print(findMedianSortedArrays([1,2],[3,4]))