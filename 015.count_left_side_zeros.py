import math

# T: O(log(n))
# S: O(1)
def count_left_side_zeros(nums):
    siz = len(nums)

    if siz==0 or nums[0]!=0:
        return 0

    low, high = 0, siz-1

    while low < high:
        mid = math.ceil((low + high) / 2)

        if nums[mid] == 0:
            low = mid
        else:
            high = mid - 1

    return low + 1



for ind, item in enumerate(([1, 2, 3, 4], 
                            [], 
                            [0, 0, 0, 0, 0, 1, 2, 3],
                            [0, 0, 0, 0, 0],
                            [0, 0, 1, 1, 2],
                        )):
    print(f'case {ind + 1}: {item} <=>', count_left_side_zeros(item))