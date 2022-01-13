# Remove Element from given list
# https://leetcode.com/problems/remove-element/description/

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).


def remove_element_from_list(nums, key):
    # Time: O(n)
    # Space: O(1)
    # two pointer approach, first points to 0 th index, last points to last element index
    # Update the right most element value before even we decrease the index

    first, last = 0, len(nums)-1

    while nums[last] == key:
        nums[last] = '*'
        last-=1

    while first <= last:
        if nums[first] == key:
            nums[first], nums[last] = nums[last], nums[first]
            nums[last] = '*'
            last-=1
        first+=1

    return first, nums


nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element_from_list(nums, val))

nums = [3,2,2,3]
val = 3
print(remove_element_from_list(nums, val))

nums = [3,2,2,3]
val = 5
print(remove_element_from_list(nums, val))
