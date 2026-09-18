class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head

        while curr:
            if curr.child:
                next_node = curr.next

                child_head = self.flatten(curr.child)

                curr.next = child_head
                child_head.prev = curr

                curr.child = None

                last = child_head

                while last.next:
                    last = last.next

                last.next = next_node

                if next_node:
                    next_node.prev = last

            curr = curr.next

        return head