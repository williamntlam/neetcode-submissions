class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # could do letter array positions and increment
        # compare arrays with one another.
        # runtime is O(n) in this case I believe.

        anagrams_dict = {}

        for word in strs:
            letters = [0 for _ in range(26)]
            for letter in word:
                letters[ord(letter) - ord('a')] += 1

            letters_tuple = tuple(letters)

            if letters_tuple not in anagrams_dict:
                anagrams_dict[letters_tuple] = [word]
            else:
                anagrams_dict[letters_tuple].append(word)

        anagrams = []
        for key in anagrams_dict:
            anagrams.append(anagrams_dict[key])

        return anagrams
       
            