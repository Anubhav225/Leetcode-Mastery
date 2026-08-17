class Solution:
    def removeDuplicateLetters(self, s):
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        stack = []
        seen = set()

        for ch in s:
            count[ch] -= 1

            if ch in seen:
                continue

            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)