class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        elif self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value is None:
            return False
        else:
            if self.value < target:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)
            else:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    def for_each(self, cb):
        if self.right is None and self.left is None:
            return cb(self.value)
        else:
            if self.right:
                cb(self.value)
                self.right.for_each(cb)
            if self.left:
                cb(self.value)
                self.left.for_each(cb)
