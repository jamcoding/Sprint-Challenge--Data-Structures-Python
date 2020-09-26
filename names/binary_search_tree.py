class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # check if the value is less than the current node's value
        if value > self.value:
            # if there is not a left node already here
            if not self.left:
                # add the node to the left
                self.left = BSTNode(value)
            else:
                # otherwise call insert on the left node
                self.left.insert(value)
        elif value <= self.value:
            if not self.right:
                # add the node to the right
                self.right = BSTNode(value)
            else:
                # otherwise call insert on the right node
                self.right.insert(value)

    def contains(self, target):
        # if the current node is the target
        if target == self.value:
            # return True
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)