# Given an array consists of non-zero integers followed by zeros
#  find an efficient algorithm to count zeros in that array

# Follow divide and prune approach
# T: O(log(n))
# S: O(1) constant
def count_right_side_zeros(nums, siz):
    if siz == 0 or nums[siz-1] != 0:
        return 0

    low, high = 0, siz-1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] == 0:
            high = mid
        else:
            low = mid + 1
    
    return siz - low


print("Res:", count_right_side_zeros([2, 5, 4, 10, 0, 0, 0, 0], 8))
print("Res:", count_right_side_zeros([2, 5, 4, 10, 12, 4, 7, 9], 8))
print("Res:", count_right_side_zeros([2, 5, 4, 10, 12, 4, 7, 0], 8))
print("Res:", count_right_side_zeros([2, 5, 4, 10, 12, 0, 0, 0], 8))
print("Res:", count_right_side_zeros([1, 1, 0, 0, 0], 5))
print("Res:", count_right_side_zeros([], 0))