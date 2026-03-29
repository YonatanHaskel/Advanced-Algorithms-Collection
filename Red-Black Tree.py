class RBT_nil_node:
    def __init__(self):
        self.color = 'B'
        self.item = 'NIL'
        self.left = self
        self.right = self
        self.parent = self

nil = RBT_nil_node()

class RBT_node:
    def __init__(self, item, color='R'):
        self.item = item
        self.color = color
        self.left = nil
        self.right = nil
        self.parent = nil

    def __repr__(self):
        return f'{self.item}({self.color})'

def print_RBT(root):
    queue = [root]
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr_node = queue.pop(0)
            current_level.append(curr_node)
            if curr_node.left is not nil:
                queue.append(curr_node.left)
            if curr_node.right is not nil:
                queue.append(curr_node.right)
        print(", ".join(str(node) for node in current_level))

def RBT_left_rotate(root, node):
    x = node
    y = x.right
    z = y.left
    if x.parent == nil:
        root = y
        y.parent = nil
    elif x.parent.left == x:
        x.parent.left = y
        y.parent = x.parent
    else:
        x.parent.right = y
        y.parent = x.parent
    y.left = x
    x.parent = y
    x.right = z
    if z is not nil:
        z.parent = x
    return root

def RBT_right_rotate(root, node):
    x = node
    y = x.left
    z = y.right
    if x.parent == nil:
        root = y
        y.parent = nil
    elif x.parent.left == x:
        x.parent.left = y
        y.parent = x.parent
    else:
        x.parent.right = y
        y.parent = x.parent
    y.right = x
    x.parent = y
    x.left = z
    if z is not nil:
        z.parent = x
    return root

def BST_adapted_insert(root, node):
    if root is nil:
        return node
    if node.item <= root.item:
        child = BST_adapted_insert(root.left, node)
        root.left = child
        child.parent = root
    else:
        child = BST_adapted_insert(root.right, node)
        root.right = child
        child.parent = root
    return root

def RBT_insert_fixup(root, new_node):
    while new_node.parent is not nil and new_node.parent.color == 'R' and new_node != root:
        parent = new_node.parent
        grandpa = parent.parent
        if grandpa == nil:
            break
        uncle = grandpa.left if parent == grandpa.right else grandpa.right
        if uncle is not nil and uncle.color == 'R':
            parent.color = uncle.color = 'B'
            grandpa.color = 'R'
            new_node = grandpa
        else:
            if grandpa.left == parent and parent.left == new_node or grandpa.right == parent and parent.right == new_node:
                if grandpa.left == parent and parent.left == new_node:
                    root = RBT_right_rotate(root, grandpa)
                else:
                    root = RBT_left_rotate(root, grandpa)
            else:
                if grandpa.left == parent and parent.right == new_node:
                    root = RBT_left_rotate(root, parent)
                    root = RBT_right_rotate(root, grandpa)
                else:
                    root = RBT_right_rotate(root, parent)
                    root = RBT_left_rotate(root, grandpa)
            grandpa.color, parent.color = parent.color, grandpa.color
    root.color = 'B'
    return root

def RBT_insert(root, item):
    new_node = RBT_node(item, color='R')
    root = BST_adapted_insert(root, new_node)
    root = RBT_insert_fixup(root, new_node)
    return root

def BST_min(root):
    if root.left:
        return BST_min(root.left)
    else:
        return root

def RBT_min(root):
    if root.left is not nil:
        return BST_min(root.left)
    else:
        return root

def RBT_successor(root):
    if root.right is not nil:
        return RBT_min(root.right)
    else:
        print("doesn't exists")

def RBT_delete_fixup(root, double_black):
    while double_black != root and double_black.color == 'B':
        parent = double_black.parent
        if parent == nil:
            break
        sibling = parent.right if double_black == parent.left else parent.left
        if double_black == parent.left:
            if sibling is not nil and sibling.color == 'R':
                parent.color, sibling.color = sibling.color, parent.color
                RBT_left_rotate(root, parent)
                sibling = parent.right if double_black == parent.left else parent.left
            elif sibling is not nil and sibling.color == 'B' and sibling.left is not nil and sibling.left.color == 'B' and sibling.right is not nil and sibling.right.color == 'B':
                sibling.color = 'R'
                double_black = parent
            elif sibling is not nil and sibling.color == 'B' and sibling.left is not nil and sibling.left.color == 'R' and sibling.right is not nil and sibling.right.color == 'B':
                sibling.color, sibling.left.color = sibling.left.color, sibling.color
                RBT_right_rotate(root, sibling)
            elif sibling is not nil and sibling.color == 'B' and sibling.right is not nil and sibling.right.color == 'R':
                sibling.color = parent.color
                parent.color = sibling.right.color = 'B'
                RBT_left_rotate(root, parent)
                double_black = root
        else:
            if sibling is not nil and sibling.color == 'R':
                parent.color, sibling.color = sibling.color, parent.color
                RBT_right_rotate(root, parent)
                sibling = parent.right if double_black == parent.left else parent.left
            elif sibling is not nil and sibling.color == 'B' and sibling.right is not nil and sibling.right.color == 'B' and sibling.left is not nil and sibling.left.color == 'B':
                sibling.color = 'R'
                double_black = parent
            elif sibling is not nil and sibling.color == 'B' and sibling.right is not nil and sibling.right.color == 'R' and sibling.left is not nil and sibling.left.color == 'B':
                sibling.color, sibling.right.color = sibling.right.color, sibling.color
                RBT_left_rotate(root, sibling)
            elif sibling is not nil and sibling.color == 'B' and sibling.left is not nil and sibling.left.color == 'R':
                sibling.color = parent.color
                parent.color = sibling.left.color = 'B'
                RBT_right_rotate(root, parent)
                double_black = root
    if double_black.color == 'R':
        double_black.color = 'B'
    root.color = 'B'
    return root

def RBT_delete(root, deleted_node):
    if root is nil:
        return nil
    double_black = None
    def RBT_delete_helper(root, deleted_node):
        nonlocal double_black
        if root is nil:
            return nil
        if root.left is not nil and deleted_node.item < root.item:
            child = RBT_delete_helper(root.left, deleted_node)
            root.left = child
            if child is not nil:
                child.parent = root
        elif root.right is not nil and deleted_node.item > root.item:
            child = RBT_delete_helper(root.right, deleted_node)
            root.right = child
            if child is not nil:
                child.parent = root
        else:
            del_color = root.color
            if root.left is nil:
                if del_color == 'B':
                    if root is not nil and root.right.color == 'R':
                        root.right.color = 'B'
                    else:
                        double_black = root.right
                return root.right
            elif root.right is nil:
                if del_color == 'B':
                    if root.left is not nil and root.left.color == 'R':
                        root.left.color = 'B'
                    else:
                        double_black = root.left
                return root.left
            else:
                successor = RBT_successor(root)
                root.item = successor.item
                root.right = RBT_delete_helper(root.right, successor)
                if root.right is not nil:
                    root.right.parent = root
        return root
    root = RBT_delete_helper(root, deleted_node)
    if double_black:
        root = RBT_delete_fixup(root, double_black)
    return root

root = RBT_node(7, 'B')
root.left = RBT_node(5, 'R')
root.left.parent = root
root.right = RBT_node(9, 'R')
root.right.parent = root
root.right.right = RBT_node(11, 'B')
root.right.right.parent = root.right
root.right.left = RBT_node(8, 'B')
root.right.left.parent = root.right
root.left.left = RBT_node(3, 'B')
root.left.left.parent = root.left
root.left.right = RBT_node(6, 'B')
root.left.right.parent = root.left

inserted_node = 1
root = RBT_insert(root, inserted_node)
print(f'root after inserting {inserted_node}:')
print_RBT(root)

deleted_node = root.left
deleted_item = deleted_node.item
root = RBT_delete(root, deleted_node)
print(f'root after deleting {deleted_item}:')
print_RBT(root)