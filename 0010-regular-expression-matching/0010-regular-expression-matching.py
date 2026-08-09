class Solution:
    def isMatch(self, s, p):
        memo = {}

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            same = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                ans = solve(i, j + 2) or (same and solve(i + 1, j))
            else:
                ans = same and solve(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return solve(0, 0)