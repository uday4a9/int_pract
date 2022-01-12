# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def remove_duplicates_from_sorted_array_m1(nums):
    # find out the next available unique item and place it in the present location
    # T: O(n) where n is lenth(nums)
    # S: O(1)
    i, j = 0, 0

    length = len(nums)

    element = nums[0]
    while j < (length-1):
        while nums[j]<=element and j<(length-1):
            j+=1
        # Index of the next biggest element to the right
        nums[i] = nums[j-1]
        element = nums[j]
        i+=1
    nums[i] = nums[j]
    i+=1
    unique_elemnt_cnt = i

    # Fill up _ symbols from i to j positions
    while i <= j:
        nums[i] = '*'
        i+=1
   
    return unique_elemnt_cnt, nums

for nums in [[0,0,1,1,1,2,2,3,3,4], [1, 1, 2], [1, 2, 3, 4]]:
    print("ip:", nums[::], "op:", remove_duplicates_from_sorted_array_m1(nums))
