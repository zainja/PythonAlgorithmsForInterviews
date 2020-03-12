class Node(object):
    def __init__(self, data, parent_node):
        self.data = data
        self.parent_node = parent_node
        self.right_child = None
        self.left_child = None
        self.balance = 0

    def insert(self, data, parent_node):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data, parent_node)
            else:
                self.left_child.insert(data, parent_node)
        else:
            if not self.right_child:
                self.right_child = Node(data, parent_node)
            else:
                self.right_child.insert(data, parent_node)
        return parent_node

    def traverse_in_order(self):
        if self.left_child:
            self.left_child.traverse_in_order()
        print(self.data)

        if self.right_child:
            self.right_child.traverse_in_order()
        print(self.data)

    def get_min(self):
        if not self.left_child:
            return self.data
        else:
            return self.left_child.get_min()

    def get_max(self):
        if not self.right_child:
            return self.data
        else:
            return self.right_child.get_max()

class BalanceTree(object):
    def __init__(self):
        self.root_node = None
    def insert(self, data):
        parent_node = self.root_node
        if self.root_node is None:
            parent_node = Node(data, None)
            self.root_node = parent_node
        else:
            parent_node = self.root_node.insert(data, self.root_node)
        self.rebalance_tree(parent_node)

    def rebalance_tree(self, parent_node):
        self.set_balance(parent_node)

    def set_balance(self, node):
        node.balance = (self.height(node.right_child) - self.height)

    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.right_child),
                           self.height(node.left_child))
