class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n
        
        def dfs(i):
            # reached the top when we hit i >= n
            if i == n:
                return 1
            elif i > n: 
                return 0

            if memo[i] != -1:
                return memo[i]

            # from the current step, climb to i + 1 and i + 2
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]

        return dfs(0)

# n = 4
# [-1, 1, 1, -1]