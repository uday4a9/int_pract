def check_anagaram_method1(s1, s2):
    # check each character in one string is avilable in other string or not
    # Time: O(n * n)
    # space: O(n)
    if len(s1) != len(s2):
        return False

    ls1, ls2 = list(s1),list(s2)

    for char1 in ls1:
        for index, char2 in enumerate(ls2):
            if char1 == char2:
                ls2[index] = '*'
                break
    
    for item in ls2:
        if item != '*':
            return False
    return True

def check_anagaram_method2(s1, s2):
    # sort individual strings and compare
    # Time: O(n * log(n))
    # space: O(n)
    if len(s1) != len(s2):
        return False

    ss1, ss2 = ''.join(sorted(s1)), ''.join(sorted(s2))

    for i in range(len(ss1)):
        if ss1[i] != ss2[i]:
            return False
    return True

def check_anagaram_method3(s1, s2):
    # sort individual strings and compare
    # Time: O(n)
    # space: O(n) ; shrinking space we can consider O(1) 
    if len(s1) != len(s2):
        return False

    import collections
    sd1 = collections.Counter(s1)

    for item in s2:
        if item not in sd1:
            return False
        else:
            sd1[item]-=1
            if sd1[item] == 0:
                sd1.pop(item)
    return True

strings_ip = (['abcaa', 'bacaa'], ['abc', 'dba'])

for s1, s2 in strings_ip:
    if check_anagaram_method1(s1, s2):
        print(s1, s2, "are anagrams")

for s1, s2 in strings_ip:
    if check_anagaram_method2(s1, s2):
        print(s1, s2, "are anagrams")

for s1, s2 in strings_ip:
    if check_anagaram_method3(s1, s2):
        print(s1, s2, "are anagrams")
