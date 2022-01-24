# find smallest element in rotated sorted array


def find_smallest_in_rotated_sorted_array(nums):
    low, high = 0, len(nums)-1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums [high]:
            high = mid
        else:
            low = mid + 1
    
    return nums[low]


for ind, item in enumerate(([1, 2, 3, 4],
                            [5, 6, 7, 1, 2, 3, 4],
                            [7, 8, 9, 1],
                        )):
    print(f'case {ind + 1}: {item} <=>', find_smallest_in_rotated_sorted_array(item))