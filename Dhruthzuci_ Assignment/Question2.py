def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    intersection_set = set1.intersection(set2)
    intersection_list = list(intersection_set)
    return intersection_list
l1=[4,9,5]
l2=[9,4,9,8,4]
print(intersection(l1,l2))
