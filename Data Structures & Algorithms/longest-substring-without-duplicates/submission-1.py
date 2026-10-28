from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_set = set()
        start = 0

        for end in range(len(s)):
            end_char = s[end]

            while end_char in char_set:
                char_set.remove(s[start])
                start += 1

            char_set.add(end_char)

            max_length = max(max_length, end - start + 1)

        return max_length
