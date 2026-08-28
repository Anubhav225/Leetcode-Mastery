class Solution:
    def mergeKLists(self, lists):
        result = None

        for i in range(len(lists)):
            result = self.merge(result, lists[i])

        return result

    def merge(self, a, b):
        dummy = ListNode(0)
        curr = dummy

        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next

            curr = curr.next

        curr.next = a or b

        return dummy.next