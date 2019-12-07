def intersect(nums1,nums2):
    nums_li = list()
    for i in nums1:
        if i in nums2:
            nums_li.append(i)
            nums2.remove(i)
    return nums_li


if __name__ == '__main__':
    print(intersect([1,2,2,1],[2,2]))