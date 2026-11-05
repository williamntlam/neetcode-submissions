class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # have a window as big as s1.
        # keep a dictionary and keep comparing the dictionary maybe?
        # what would the runtime of this be?
        # maybe not a dictionary since comparing would be O(n)
        # maybe have a 26 indexed array representing each letter ( since it's only lowercase )
        # comparison is technically O(1) since the 26 is bounded and does not grow with the size of the input.
        # overall runtime complexity is O(n)
        # spacetime complexity is also O(1)
        
        if len(s2) < len(s1):
            return False

        s1_letters = [0 for _ in range(26)]
        for letter in s1:
            s1_letters[ord(letter) - ord('a')] += 1

        window_letters = [0 for _ in range(26)]
        for letter_index in range(len(s1)):
            current_letter = s2[letter_index]
            window_letters[ord(current_letter) - ord('a')] += 1

        right = len(s1)
        left = 0

        while left <= len(s2) - 1 and right <= len(s2) - 1:
            if window_letters == s1_letters:
                return True
            
            window_letters[ord(s2[right]) - ord('a')] += 1
            window_letters[ord(s2[left]) - ord('a')] -= 1
            
            left += 1
            right += 1

        return window_letters == s1_letters