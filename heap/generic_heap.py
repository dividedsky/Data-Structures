class Heap:
    def __init__(self, comparator=max):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)
        print("after insert:", self.storage)

    def delete(self):
        print("before delete:", self.storage)
        if len(self.storage) > 0:
            val = self.storage.pop(0)
            if len(self.storage):
                end = self.storage.pop()
                self.storage.insert(0, end)
                self._sift_down(0)
            print("after delete:", self.storage)
            return val

    def get_priority(self):
        print(self.storage)
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index > 0:
            parent_idx = (index - 1) // 2
            if (
                self.comparator(self.storage[index], self.storage[parent_idx])
                == self.storage[index]
            ):
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
        if not right or self.comparator(left, right) == left:
            priority_idx = left_idx
            priority_val = left
            # self.storage[index], self.storage[left_idx] = (
            #     self.storage[left_idx],
            #     self.storage[index],
            # )
            # self._sift_down(left_idx)
        else:
            priority_idx = right_idx
            priority_val = right
            # self.storage[index], self.storage[right_idx] = (
            #     self.storage[right_idx],
            #     self.storage[index],
            # )
            # self._sift_down(right_idx)
        if self.comparator(self.storage[index], priority_val) == priority_val:
            self.storage[index], self.storage[priority_idx] = (
                self.storage[priority_idx],
                self.storage[index],
            )
            self._sift_down(priority_idx)
