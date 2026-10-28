from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_map = defaultdict(int)
        start = 0

        for end in range(len(s)):
            end_char = s[end]
            char_map[end_char] += 1

            while char_map[end_char] > 1 and start <= end:
                char_map[s[start]] -= 1
                if char_map[s[start]] <= 0:
                    del char_map[s[start]]

                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
