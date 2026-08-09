class Solution:
    def shortestPalindrome(self, s):
        rev = s[::-1]
        text = s + "#" + rev

        table = [0] * len(text)

        for i in range(1, len(text)):
            j = table[i - 1]

            while j > 0 and text[i] != text[j]:
                j = table[j - 1]

            if text[i] == text[j]:
                j += 1

            table[i] = j

        length = table[-1]
        return rev[:len(s) - length] + s