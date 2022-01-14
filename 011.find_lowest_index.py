# return the lowest index of a key in given sorted array

def find_lowest_index_m1(nums, key):
    # T: O(log(n) + n/2) = O(n + log(n))
    # S: O(1) constant
    low, high = 0, len(nums)-1
    index = float('-Inf')

    while low <= high:
        mid = (low + high) // 2

        if key < nums[mid]:
            high = mid-1
        elif key > nums[mid]:
            low  = mid+1
        else:
            index=mid
            # her we do reverse travel and returns least index
            while mid>0 and nums[mid-1]==key:
                index = mid
                mid-=1
            break
    
    return index

def find_lowest_index_m2(nums, key):
    # T: O(log(n))
    # S: O(1)
    # Here, as mid parameter changing to right most element
    #  while loop should run till low < high
    #  For last element comparison we should use additonal check
    low, high = 0, len(nums)-1

    while low < high:
        mid = (low + high) // 2

        if key < nums[mid]:
            high = mid-1
        elif key > nums[mid]:
            low  = mid+1
        else:
            high = mid
    return low if nums[low] == key else float('-Inf')

nums = [1, 3, 5, 6, 7, 8, 8, 9]
for ind, key in enumerate([8, 12, -2, 1]):
    print(f"-- case{ind+1}:")
    print("m1:", find_lowest_index_m1(nums, key))
    print("m2:", find_lowest_index_m2(nums, key))