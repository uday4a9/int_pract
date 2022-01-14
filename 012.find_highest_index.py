# return the highest index of a key in given sorted array

import math 

def find_highest_index(nums, key):
    # T: O(log n)
    # S: O(1) constant

    # Key point here is to find out the breaking condition of the loop
    # When exactly item found we need to move marker to the ceil index
    # rather than floor index
    low, high = 0, len(nums)-1

    while low < high:
        mid = math.ceil((low + high) / 2)

        if key < nums[mid]:
            high = mid-1
        elif key > nums[mid]:
            low  = mid+1
        else:
            low = mid
    return low if nums[low] == key else float('-Inf')


    

nums = [1, 3, 5, 6, 7, 8, 8, 9]
for ind, key in enumerate([8, 12, -2, 1]):
    print(f"-- case{ind+1}:")
    print("m1:", find_highest_index(nums, key))