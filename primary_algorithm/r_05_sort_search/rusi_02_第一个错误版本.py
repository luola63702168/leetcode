def firstBadVersion(n):
    left = 0
    right = n
    # isBadVersion = None
    while True:
        mid = (left + right) // 2
        if isBadVersion(mid) is False and isBadVersion(mid + 1) is True:
            return mid + 1
        if isBadVersion(mid) is False and isBadVersion(mid + 1) is False:
            left = mid
        if isBadVersion(mid) is True and isBadVersion(mid + 1) is True:
            right = mid
