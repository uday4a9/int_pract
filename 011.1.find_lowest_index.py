# Find lowest index of element `key` in given sorted array/list
# nums = [1, 3, 5, 6, 7, 8, 8, 9]

def find_lowest_index(lst, key):
    low, high = 0, len(lst)-1
     
    # instead this we can use bisect.bisect_left function
    while low < high:
        mid = (low + high) // 2
        if lst[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low  if lst[low] == key else float('-Inf')

lst = ( 
    ([1, 3, 5, 6, 7, 8, 8, 9], 8),
    ([1, 3, 4, 6, 7, 8, 8, 9], 3),
    ([1, 3, 3, 6, 7, 8, 8, 9], 2),
    ([1, 3, 3, 6, 7, 8, 8, 9], 9),
    ([-1, 1, 1, 1, 1, 1], 1),
)


for item in lst:
    print("Ind:", find_lowest_index(*item))
    print('*' * 25)
