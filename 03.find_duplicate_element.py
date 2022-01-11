# P: Find a duplicate element in a given array,
#   Array contains 1..n-1 elements, where n is length of the array

def find_duplicate_item_m1(l):
    # scan element by element and forward postioned array compare
    # Time: O(n^2)
    # Space: O(1) 

    length = len(l)
    for i in range(length):
        for j in range(i+1, length):
            if l[i] == l[j]:
                return l[i]
    return float('-Inf')

def find_duplicate_item_m2(l):
    # sort and compare adjacent elements
    # Time: O(nlogn)
    # Space: O(1) 

    l.sort()
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return l[i]
    return float('-Inf')

def find_duplicate_item_m3(l):
    # take an auxiliary array and fill up with False update on visit to True
    # Time: O(n)
    # Space: O(n) 

    status = [False] * (len(l) + 1)
    
    for i in range(len(l)):
        if status[l[i]]:
            return l[i]
        status[l[i]] = True
    return float('-Inf')

def find_duplicate_item_m4(l):
    # Do the inplace negation as all numbers range [1...n-1]
    # Time: O(n)
    # Space: O(1)
    for i in range(len(l)):
        item_index = abs(l[i])
        if l[item_index] < 0:
            return item_index
        l[item_index] *= -1
    return float('-Inf')

l1 = [4, 2, 3, 1, 2]
val = find_duplicate_item_m4(l1)
print(None if val==float('-Inf') else val)
l2 = [4, 2, 3, 1, 0]
val = find_duplicate_item_m4(l2)
print(None if val==float('-Inf') else val)