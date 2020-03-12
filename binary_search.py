class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            if not self.right_child:
                self.right_child = Node(data)
            else:
                self.left_child.insert(data)

    def get_min(self):
        if self.left_child is None:
            return self.data
        else:
            return self.get_min()

    def get_max(self):
        if self.right_child is None:
            return self.data
        else:
            return self.get_max()

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child().traverse_in_order()
        print(self.data)

        if self.right_child is not None:
            return self.right_child().traverse_in_order()
        print(self.data)

    def remove(self, data, parent_node):
        if data < self.data:
            if self.left_child is not None:
                self.left_child.remove(data, self)
        elif data > self.data:
            if self.right_child is not None:
                self.right_child.remove(data, self)
        else:
            if self.left_child is not Node and self.right_child is not None:
                self.data = self.right_child.getMin()
                self.right_child.remove(self.data, self)

            elif parent_node.left_child is not None:
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child
                parent_node = self.right_child
            elif parent_node.right_child == self:
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child
                parent_node.right_child = temp_node


class BST(object):
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if not self.root_node:
            self.root_node = Node(data)
        else:
            self.root_node.insert(data)

    def remove(self, data):
        if self.root_node:
            if self.root_node.data == data:
                temp_node = Node(None)
                temp_node.left_child = self.root_node
                self.root_node.remove(data, temp_node)
            else:
                self.root_node.remove(data, None)

    def get_max(self):
        if self.root_node:
            return self.root_node.get_max()

    def get_min(self):
        if self.root_node:
            return self.root_node.get_min()

    def traverse_in_order(self):
        if self.root_node:
            self.root_node.traverse_in_order()


bst = BST()
bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)
bst.remove(1)
bst.remove(12)
bst.traverse_in_order()