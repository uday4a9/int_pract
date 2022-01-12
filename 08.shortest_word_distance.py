# https://leetcode.com/problems/shortest-word-distance/#

# Note: the two words will be existed in the given input list of words
# in given list of words and two words are given, findout the shortest distance
# Ex: words = ["a", "b", "c", "d", "e"]
# w1='d',  w2='a'   
    # -> distance: 3
# w1='b', w2='d' 
    # -> distance: 1

#Ex2:
# words = ["a", "c", "b", "c", "a", "b"]
# w1="a", w2="b"  -> should return 1 instead of 2

def shortest_distance_bw_words_m1(words, w1, w2):
    #  This solution works if and only if no words are repeating
    # T: O(w) + O(1)
    # S: O(w) w=length of the words
    result = {}
    for index, word in enumerate(words):
        result[word] = index

    return result[w1], result[w2]

# If the words in a list are repeating
def shortest_distance_bw_words_m2(words, w1, w2):
    #  use two pointer approach
    # T: O(w) total number of items in word list
    # S: O(2) i.e constant
    marker = float('-Inf')
    first = marker
    second = marker

    for index, word in enumerate(words):
        if word == w1:
            if first == marker:
                first = index
            
            if second != marker and abs(index-second) <= abs(first-second):
                first = index
        elif word == w2:
            if second == marker:
                second = index
            
            if first != marker and abs(first-index) <= abs(first-second):
                second = index
    return (first, second)


words = ["a", "b", "c", "d", "e"]
w1='d'
w2='a'
print(shortest_distance_bw_words_m1(words, w1, w2))

words = ["a", "c", "b", "c", "a", "b"]
w1, w2 = 'a', 'b'
print(shortest_distance_bw_words_m2(words, w1, w2))

words = ["a", "c", "b", "c", "a"]
w1, w2 = 'a', 'b'
print(shortest_distance_bw_words_m2(words, w1, w2))

words = ["c", "a", "b", "c", "a"]
w1, w2 = 'a', 'b'
print(shortest_distance_bw_words_m2(words, w1, w2))