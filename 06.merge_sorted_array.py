# https://leetcode.com/problems/merge-sorted-array/
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge_nums2_to_nums1(nums1, nums2, m, n):
    # T: O(n); n is length(nums1)
    # S: O(1)
    last_index = len(nums1) - 1

    while m>0 and n>0:
        if nums1[m-1] <= nums2[n-1]:
            nums1[last_index] = nums2[n-1]
            n -= 1
            last_index -= 1
        elif nums1[m-1] > nums2[n-1]:
            nums1[last_index] = nums1[m-1]
            m -= 1
            last_index -= 1
        else:
            m -= 1
            n -= 1


        

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge_nums2_to_nums1(nums1, nums2, m, n)
print(nums1)

nums1 = [1,3,5,0,0,0]
m = 3
nums2 = [2,4,6]
n = 3
merge_nums2_to_nums1(nums1, nums2, m, n)
print(nums1)