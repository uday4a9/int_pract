# IP: ALL IS WELL
# OP: LLA SI LLEW

def reverse_words_m1(string):
    # split string into words
    # It will use plenty of auxiliary space to store the each word
    # and reversing operation

    # n is the length of the string
    # w is individual word, K is the length of the same 
    # T: o(n * w * K)
    # Assume if string contains only one word 
    # O( 1 * 1 * K) ; k is the length of the word
    # S: O(n) auxiliary space
    return ' '.join([word[::-1] for word in string.split(' ')])\

def reverse_(lst, first, last):
    while first < last:
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1

def reverse_words_m2(string):
    # as python strings are immutable let me convert it to list
    # T: O(n)
    # S: O(1)
    lst = list(string)

    # scan from left to right
    first_index = 0
    for i in range(len(string)):
        if lst[i] == ' ':
            reverse_(lst, first_index, i-1)
            first_index = i + 1
    reverse_(lst, first_index, len(string)-1)
    return ''.join(lst)

s = 'ALL IS WELL'
print(reverse_words_m1(s))
print(reverse_words_m2(s))