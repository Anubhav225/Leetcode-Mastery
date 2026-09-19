from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        self.values = {}
        self.freq = {}
        self.groups = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1

        self.update_freq(key)

        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.values:
            self.values[key] = value
            self.update_freq(key)
            return

        if self.size == self.capacity:
            old_key, _ = self.groups[self.min_freq].popitem(last=False)

            del self.values[old_key]
            del self.freq[old_key]

            self.size -= 1

        self.values[key] = value
        self.freq[key] = 1
        self.groups[1][key] = True

        self.min_freq = 1
        self.size += 1

    def update_freq(self, key):
        old_freq = self.freq[key]

        del self.groups[old_freq][key]

        if not self.groups[old_freq]:
            del self.groups[old_freq]

            if self.min_freq == old_freq:
                self.min_freq += 1

        new_freq = old_freq + 1

        self.freq[key] = new_freq
        self.groups[new_freq][key] = True