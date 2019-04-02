import math


class Heap:
    def __init__(self):
        self.storage = []

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

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index > 0:
            parent_idx = (index - 1) // 2

            if self.storage[parent_idx] < self.storage[index]:
                self.storage[parent_idx], self.storage[index] = (
                    self.storage[index],
                    self.storage[parent_idx],
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
        if not right or left > right:
            self.storage[index], self.storage[left_idx] = (
                self.storage[left_idx],
                self.storage[index],
            )
            self._sift_down(left_idx)
        else:
            self.storage[index], self.storage[right_idx] = (
                self.storage[right_idx],
                self.storage[index],
            )
            self._sift_down(right_idx)
