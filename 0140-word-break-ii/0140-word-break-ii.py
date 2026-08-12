class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        memo = {}

        def solve(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            result = []

            for word in words:
                if s.startswith(word, start):
                    parts = solve(start + len(word))

                    for part in parts:
                        if part == "":
                            result.append(word)
                        else:
                            result.append(word + " " + part)

            memo[start] = result
            return result

        return solve(0)