# find an element in 2d sorted matrix

def find_element_in_2d_matrix_m2(nums, n, key):
    # T: O(log(n))
    # S: O(1)

    # Apply binary search logic on full array where length is (n*n)
    # 

    total = n * n

    low, high = 0, total-1

    while low <= high:
        mid = (low + high) // 2

        row, col = mid // n, mid % n

        if key < nums[row][col]:
            high = mid-1
        elif key > nums[row][col]:
            low=mid+1
        else:
            return (row, col)
    
    return float('-Inf')

l =[
    [2, 4, 6, 8],
    [12, 14, 16, 18],
    [22, 24, 26, 28],
    [32, 34, 36, 38]
]
key = 18

from pprint import pprint
pprint(l)
for key in [18, 21]:
    res = find_element_in_2d_matrix_m2(l, 4, key)
    if res == float('-Inf'):
        print(key," not found in matrix")
    else:
        print(key, "found at location:", res)