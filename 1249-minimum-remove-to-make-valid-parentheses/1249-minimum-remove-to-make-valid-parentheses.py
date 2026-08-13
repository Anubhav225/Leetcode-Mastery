class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        open = 0

        for ch in s:
            if ch == '(':
                open += 1
                result.append(ch)
            elif ch == ')':
                if open > 0:
                    open -= 1
                    result.append(ch)
            else:
                result.append(ch)

        final = []
        
        for ch in reversed(result):
            if ch == '(' and open > 0:
                open -= 1
            else:
                final.append(ch)

        return ''.join(reversed(final))