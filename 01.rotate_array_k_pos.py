def right_rotate_array_by_k_pos_1(elements, k):
    # move element by element
    # time: o(K * n) ; where as n is no. of elements
    # space: O(1); as we are using only one variable
    last_index = len(elements) - 1

    for i in range(k):
        tmp = elements[last_index]
        for i in reversed(range(1,len(elements))):
            elements[i] = elements[i-1]
        elements[0] = tmp


def right_rotate_array_by_k_pos_2(elements, k):
    # add an auxiliary array and copy the elements to new pos
    # Time: O(n)  ; n is total number of elements
    # Space: O(n) ; As we are using auxiliary array
    total_num_of_elements = len(elements)

    tmp = [0 for _ in range(total_num_of_elements)]

    for i in range(total_num_of_elements):
        new_pos = i + k
        tmp[new_pos %total_num_of_elements] = elements[i]
    
    for i in range(total_num_of_elements):
        elements[i] = tmp[i]


def reverse_(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i = i+1
        j = j-1

def right_rotate_array_by_k_pos_3(elements, k):
    # add an auxiliary array and copy the elements to new pos
    # Time: O(n)  ; n is total number of elements
    # Space: O(1) ; 

    # 1. reverse the whole
    reverse_(elements, 0, len(elements) - 1)

    # 2. reverse the first k elements
    reverse_(elements, 0, k - 1)

    # 3. rever elements from k till end of list
    reverse_(elements, k, len(elements) - 1)


l1 = [1, 2, 3, 4, 5, 6, 7]
right_rotate_array_by_k_pos_1(l1, 3)
print(l1)

l2 = [1, 2, 3, 4, 5, 6, 7]
right_rotate_array_by_k_pos_2(l2, 3)
print(l2)

l3 = [1, 2, 3, 4, 5, 6, 7]
right_rotate_array_by_k_pos_3(l3, 3)
print(l3)
