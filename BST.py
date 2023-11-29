class BSTNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self._add_child(data, self.root)

    def _add_child(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data, parent=node)
            else:
                self._add_child(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = BSTNode(data, parent=node)
            else:
                self._add_child(data, node.right)

    def get_max(self):
        if self.root is None:
            return None

        return self._get_right_child(self.root).data

    def _get_right_child(self, node):
        if node.right is None:
            return node
        return self._get_right_child(node.right)

    def get_min(self):
        if self.root is None:
            return None

        return self._get_left_child(self.root).data

    def _get_left_child(self, node):
        if node.left is None:
            return node
        return self._get_left_child(node.left)

    def traverse_in_order(self, node, traversed_data):
        if node is not None:
            self.traverse_in_order(node.left, traversed_data)
            traversed_data.append(node.data)
            self.traverse_in_order(node.right, traversed_data)

    def delete(self, data):
        if self.root is None:
            return None

        self._remove_node(data, self.root)

    def _remove_node(self, data, node):
        if node is None:
            return None

        if data < node.data:
            self._remove_node(data, node.left)
        elif data > node.data:
            self._remove_node(data, node.right)
        else:
            if node.left is None and node.right is None:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
                del node
            elif node.left is None and node.right is not None:
                node.data = node.right.data
                node.right = None
            elif node.right is None and node.left is not None:
                node.data = node.left.data
                node.left = None
            else:
                predecessor = self._get_predecessor(node.left)
                node.data = predecessor.data
                self._remove_node(predecessor.data, predecessor)

    def _get_predecessor(self, node):
        if node.right is not None:
            return self._get_predecessor(node.right)
        return node

    def traverse_pre_order(self, node, traversed_data):
        if node is not None:
            traversed_data.append(node.data)
            self.traverse_pre_order(node.left, traversed_data)
            self.traverse_pre_order(node.right, traversed_data)

    def traverse_post_order(self, node, traversed_data):
        if node is not None:
            self.traverse_post_order(node.left, traversed_data)
            self.traverse_post_order(node.right, traversed_data)
            traversed_data.append(node.data)
