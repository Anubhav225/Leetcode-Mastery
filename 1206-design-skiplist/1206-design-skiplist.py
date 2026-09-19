import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * level


class Skiplist:

    def __init__(self):
        self.max_level = 16
        self.head = Node(-1, self.max_level)

    def random_level(self):
        level = 1

        while random.random() < 0.5 and level < self.max_level:
            level += 1

        return level

    def search(self, target: int) -> bool:
        cur = self.head

        for level in range(self.max_level - 1, -1, -1):
            while cur.next[level] and cur.next[level].value < target:
                cur = cur.next[level]

        cur = cur.next[0]

        return cur is not None and cur.value == target

    def add(self, num: int) -> None:
        update = [None] * self.max_level
        cur = self.head

        for level in range(self.max_level - 1, -1, -1):
            while cur.next[level] and cur.next[level].value < num:
                cur = cur.next[level]

            update[level] = cur

        level = self.random_level()
        node = Node(num, level)

        for i in range(level):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        cur = self.head

        for level in range(self.max_level - 1, -1, -1):
            while cur.next[level] and cur.next[level].value < num:
                cur = cur.next[level]

            update[level] = cur

        cur = cur.next[0]

        if cur is None or cur.value != num:
            return False

        for i in range(len(cur.next)):
            if update[i].next[i] != cur:
                break

            update[i].next[i] = cur.next[i]

        return True