class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                for word in words:
                    if s[i:i + len(word)] == word:
                        dp[i + len(word)] = True

        return dp[len(s)]