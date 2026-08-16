class Solution:
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        while k:
            stack.pop()
            k -= 1

        answer = "".join(stack).lstrip("0")

        return answer if answer else "0"