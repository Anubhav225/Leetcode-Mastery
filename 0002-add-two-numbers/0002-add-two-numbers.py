class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry

            cur.next = ListNode(total % 10)
            carry = total // 10

            cur = cur.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next