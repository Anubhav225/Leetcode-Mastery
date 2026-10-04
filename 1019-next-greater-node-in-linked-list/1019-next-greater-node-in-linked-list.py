
class Solution:
    def nextLargerNodes(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        answer = [0] * len(nums)
        stack = []

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                answer[index] = nums[i]

            stack.append(i)

        return answer