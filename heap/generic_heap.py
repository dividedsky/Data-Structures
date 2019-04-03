class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) > 0:
            val = self.storage.pop(0)
            if len(self.storage):
                end = self.storage.pop()
                self.storage.insert(0, end)
                self._sift_down(0)
            return val

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index > 0:
            parent_idx = (index - 1) // 2
            if self.comparator(self.storage[index], self.storage[parent_idx]):
                self.storage[index], self.storage[parent_idx] = (
                    self.storage[parent_idx],
                    self.storage[index],
                )
                self._bubble_up(parent_idx)

    def _sift_down(self, index):
        left_idx = index * 2 + 1
        right_idx = index * 2 + 2
        try:
            left = self.storage[left_idx]
        except IndexError:
            left = None
        try:
            right = self.storage[right_idx]
        except IndexError:
            right = None
        if not left and not right:
            return None  # return if we are at a leaf
        if not right or self.comparator(left, right):
            priority_idx = left_idx
            priority_val = left
        else:
            priority_idx = right_idx
            priority_val = right
        if self.comparator(priority_val, self.storage[index]):
            self.storage[index], self.storage[priority_idx] = (
                self.storage[priority_idx],
                self.storage[index],
            )
            self._sift_down(priority_idx)
