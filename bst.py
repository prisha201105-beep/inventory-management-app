class Node:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, item_id, name, price):
        self.root = self._insert(self.root, item_id, name, price)

    def _insert(self, root, item_id, name, price):
        if root is None:
            return Node(item_id, name, price)
        if item_id < root.item_id:
            root.left = self._insert(root.left, item_id, name, price)
        elif item_id > root.item_id:
            root.right = self._insert(root.right, item_id, name, price)
        return root

    def search(self, item_id):
        return self._search(self.root, item_id)

    def _search(self, root, item_id):
        if root is None or root.item_id == item_id:
            return root
        if item_id < root.item_id:
            return self._search(root.left, item_id)
        return self._search(root.right, item_id)

    def delete(self, item_id):
        self.root = self._delete(self.root, item_id)

    def _delete(self, root, item_id):
        if root is None:
            return root
        if item_id < root.item_id:
            root.left = self._delete(root.left, item_id)
        elif item_id > root.item_id:
            root.right = self._delete(root.right, item_id)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._minValueNode(root.right)
            root.item_id = temp.item_id
            root.name = temp.name
            root.price = temp.price
            root.right = self._delete(root.right, temp.item_id)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self):
        items = []
        self._inorder(self.root, items)
        return items

    def _inorder(self, root, items):
        if root:
            self._inorder(root.left, items)
            items.append({"id": root.item_id, "name": root.name, "price": root.price})
            self._inorder(root.right, items)
