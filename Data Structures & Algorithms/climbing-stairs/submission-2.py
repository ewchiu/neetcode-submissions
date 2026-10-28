class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        
        def dfs(i):
            # reached the top when we hit i >= n
            if i >= n:
                return i == n

            if cache[i] != -1:
                return cache[i]

            # from the current step, climb to i + 1 and i + 2
            cache[i] = dfs(i + 1) + dfs(i + 2)

            # add results to the cache
            return cache[i]

        return dfs(0)