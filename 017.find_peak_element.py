# https://leetcode.com/problems/find-peak-element/description/

# You can assume that beyond elements are -Inf on both ends

# T: O(log(n))
# S: O(1)
def find_peak_element(nums):
    low, high = 0, len(nums)-1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums[mid+1]:
            low = mid + 1
        else:
            high = mid

    return nums[low]


for ind, item in enumerate(([1, 2, 3, 4],
                            [1,2,1,3,5,6,4],
                            [1, 8, 9, 3, 7, 5],
                            [9, 8, 7, 6, 5],
                            [9, 10, 7, 6, 5],
                        )):
    print(f'case {ind + 1}: {item} <=>', find_peak_element(item))