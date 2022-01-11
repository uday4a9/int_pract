# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def find_anagram_indices_m1(mstr, sstr):
    # Generate possible substrings and verify each substring
    # is anagram or not.

    # for a n length string, n-w words can be generated 
    # w = length of word
    # w * log(w) is for sorting

    # T: O((n-(w-1)) * w * log(w)) similar to O(nw)
    # S: O(w)
    length_of_sstr = len(sstr)
    length_of_mstr = len(mstr)
    output = []

    i = 0
    while True:
        if i > (length_of_mstr - length_of_sstr):
            break

        new_sstring = mstr[i: i+length_of_sstr]
        if is_anagram(new_sstring, sstr):
            output.append(i)
        i+=1
    return output

s = "cbaebabacd"
p = "abc"
print(find_anagram_indices_m1(s, p))