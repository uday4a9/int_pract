# implement binary search

marker = float('-Inf')
def binary_search(nums, key):
    # T: O(log(n))
    # S: (1) constant

    low, high = 0, len(nums)-1

    while low<high:
        mid = (low + high) // 2 

        if key < nums[mid]:
            high = mid-1
        elif key > nums[mid]:
            low = mid+1
        else: # element found
            return mid
    return float('-Inf')

l = [5, 10, 25, 30, 35, 40, 45, 50]

for key in [45, 48]:
    index = binary_search(l, key)
    if index == marker:
        print(key, "Not found")
    else:
        print(key, "found at index:", index)

