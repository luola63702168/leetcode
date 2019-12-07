def merge(nums1, m, nums2, n):
    if n == 0:
        nums1[:] = nums1+nums2
    else:
        nums1[:] = nums1[:-n] + nums2
    nums1.sort()
    return nums1

if __name__ == '__main__':
    print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
    print(merge([1],1,[],0,))