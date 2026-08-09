class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)

        for i in range(1, n):
            if n % i == 0:
                part = s[:i]

                if part * (n // i) == s:
                    return True

        return False