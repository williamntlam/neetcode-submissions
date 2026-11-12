class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        # have a left and right pointer
        # could start at a letter that is present in t.
        # for instance, as we're searching s we should only start searching / recording
        # if it's a letter in t.

        # what if i moved the left, until i hit a letter that's in t.
        # then i move the right and keep moving left until i hit left
        # from there, i keep iterating left and repeat the process?

        # can't i collect all letters,  in t from s, and then keep iterating left forward and back backwards based on the indexes?
        # for example, i can save the backward and forward indices.

        need = {}
        window = {}

        # Count required characters in t
        for char in t:
            need[char] = need.get(char, 0) + 1

        left = 0
        formed = 0
        required = len(need)

        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            char = s[right]

            # Step 1: Expand right
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            # Step 2: Shrink left while valid
            while formed == required:
                # Update shortest substring
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # Remove leftmost character
                left_char = s[left]
                window[left_char] -= 1

                # Check if window becomes invalid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]

    
        