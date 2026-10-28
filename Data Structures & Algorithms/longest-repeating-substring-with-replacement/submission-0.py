from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = defaultdict(int)
        start = 0
        max_length = 0
        max_freq = 0

        for end in range(len(s)):
            char_map[s[end]] += 1
            max_freq = max(max_freq, char_map[s[end]])

            while (end - start + 1) - max_freq > k:
                char_map[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)

        return max_length
        