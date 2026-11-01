class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force solution, find all possible
        # combinations and take the longest length
        # O(n^2) * O(n) = O(n^3)

        # O(n) solution,
        # scan through once and use sliding window.

        # go through algorithm first.
        # 

        # keep track of k
        frequency = {}
        max_frequency_char = None
        max_frequency = 0
        current_letter = s[0]
        max_k = k

        max_length = 0

        # need to be careful of current_letter and when k decrements or increments.

        left = 0
        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            if frequency[s[right]] > max_frequency:
                max_frequency = frequency[s[right]]
                max_frequency_char = s[right]

            replacements = right - left + 1 - max_frequency

            if replacements > k:
                # move left
                while replacements > k:
                    frequency[s[left]] = frequency.get(s[left], 0) - 1
                    left += 1

                    max_frequency = max(frequency.values())
                    replacements = (right - left + 1) - max_frequency

            max_length = max(max_length, right - left + 1)

        return max_length