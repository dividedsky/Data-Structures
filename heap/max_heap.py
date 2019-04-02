import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) > 1:
            print(self.storage)
            self.storage.pop(0)
            self.storage = [self.storage.pop()] + self.storage
            self._sift_down(0)

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while self.storage[math.floor((index - 1) / 2)] < self.storage[index]:
            self.storage[math.floor((index - 1) / 2)], self.storage[index] = (
                self.storage[index],
                self.storage[math.floor((index - 1) / 2)],
            )

    def _sift_down(self, index):
        while self.storage[index] < max(
            self.storage[index * 2 + 2], self.storage[index * 2 + 1]
        ):
            if self.storage[index * 2 + 2] > self.storage[index]:
                self.storage[index * 2 + 2], self.storage[index] = (
                    self.storage[index],
                    self.storage[index * 2 + 2],
                )
            else:
                self.storage[index * 2 + 1], self.storage[index] = (
                    self.storage[index],
                    self.storage[index * 2 + 1],
                )
