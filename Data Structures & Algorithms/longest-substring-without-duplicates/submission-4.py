class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        letter_positions = {}

        for right in range(len(s)):
            current_letter = s[right]
            if current_letter not in letter_positions:
                letter_positions[current_letter] = right
            else:
                if letter_positions[current_letter] >= left:
                    left = letter_positions[current_letter] + 1
                letter_positions[current_letter] = right

            max_length = max(max_length, right - left + 1)
        
        return max_length