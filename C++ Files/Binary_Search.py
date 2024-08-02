#1) Binary_Search

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        midI = (low + high)//2
        if nums[midI] == target:
            return midI
        elif nums[midI] > target:
            high = midI - 1
        else:
            low = midI + 1
    return -1
    
def Generic_Bin_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# Problem-1 (Count min number of rotations to make list sorted)
def count_rot(lst):
    if len(lst) == 0 or len(lst) == 1:
        return 0
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            return 1
        else:
            return 0
    else:
        n = len(lst)
        midI = n//2
        while 0 <= midI and midI < len(lst):
            mid = lst[midI]
            if (midI == 0 and lst[midI + 1] < mid) or (mid > lst[midI + 1] and mid > lst[midI - 1]):
                return midI + 1
            elif (midI == n - 1 and mid > lst[midI - 1]) or (mid < lst[midI + 1] and mid < lst[midI - 1]):
                return midI
            elif mid < lst[midI + 1] and mid > lst[midI - 1]:
                midI = midI - 1
            else:
                midI = midI + 1



