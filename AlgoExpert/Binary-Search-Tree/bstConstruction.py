class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(log(n)) space
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(self.value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(self.value, self)
        else:
            # has 2 children
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
