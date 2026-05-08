# ==========================================================
# BINARY SEARCH TREE (BST)
# ==========================================================

# Operations:
# 1. Insert
# 2. Search
# 3. Delete
# 4. Inorder Traversal


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None


    # ------------------------------------------------------
    # INSERT
    # ------------------------------------------------------

    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)

        else:
            root.right = self.insert(root.right, key)

        return root


    # ------------------------------------------------------
    # SEARCH
    # ------------------------------------------------------

    def search(self, root, key):

        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)


    # ------------------------------------------------------
    # FIND MINIMUM VALUE NODE
    # ------------------------------------------------------

    def min_value_node(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current


    # ------------------------------------------------------
    # DELETE
    # ------------------------------------------------------

    def delete(self, root, key):

        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:

            # Node with one child or no child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.min_value_node(root.right)

            root.data = temp.data

            root.right = self.delete(root.right, temp.data)

        return root


    # ------------------------------------------------------
    # INORDER TRAVERSAL
    # ------------------------------------------------------

    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)



# ==========================================================
# DRIVER CODE
# ==========================================================

bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("Inorder Traversal:")
bst.inorder(bst.root)

print("\n")

# Search
key = 40

if bst.search(bst.root, key):
    print(key, "found in BST")
else:
    print(key, "not found")

# Delete
bst.root = bst.delete(bst.root, 70)

print("\nInorder after deleting 70:")
bst.inorder(bst.root)