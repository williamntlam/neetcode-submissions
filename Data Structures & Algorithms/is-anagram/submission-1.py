class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same characters, same number of times, order doesn't matter
        # use dictionary

        # run time is O(2 * n) which simplifies to O(n)

        dict_s = {}
        for letter in s:
            if letter not in dict_s:
                dict_s[letter] = 1
            else:
                dict_s[letter] += 1

        dict_t = {}
        for letter in t:
            if letter not in dict_t:
                dict_t[letter] = 1
            else:
                dict_t[letter] += 1

        return dict_s == dict_t