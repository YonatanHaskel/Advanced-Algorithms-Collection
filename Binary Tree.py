class node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __repr__(self):
        return f"node({self.item})"

def height(root):
    if root is None:
        return 0
    r_height, l_height = height(root.right), height(root.left)
    return max(r_height, l_height) + 1


def balancedTree(root):
    if root is None:
        return True
    r_height, l_height = height(root.right), height(root.left)
    if abs(r_height - l_height) == 0 or abs(r_height - l_height) == 1:
        return (balancedTree(root.right)) and (balancedTree(root.left))
    return False


def perfecTree(root):
    if root is None:
        return False
    if root.right is not None and root.left is not None:
        return (perfecTree(root.right)) and (perfecTree(root.left))
    return False


def crockedTree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is None:
        return crockedTree(root.left)
    if root.right is not None and root.left is None:
        return crockedTree(root.right)
    if root.left.right is not None or root.right.left is not None:
        return False
        return (crockedTree(root.left)) and (crockedTree(root.right))
    return False


def fullTree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return (fullTree(root.right)) and (fullTree(root.left))
    if root.left is not None and root.right is not None:
        return (fullTree(root.right)) and (fullTree(root.left))
    return False


def swapTree(root):
    if root is None:
        return ()
    root.right, root.left = root.left, root.right
    return (swapTree(root.left)) and (swapTree(root.right))


def print_Tree_by_levels(root):
    if root is None:
        print("None")
        return
    queue = [root]
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr_node = queue.pop(0)
            current_level.append(str(curr_node.item))
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        print(", ".join(current_level))


def BST_search(root, target):
    if root is None:
        return None
    if target.item == root.item:
        return root.item
    elif target.item < root.item:
        return BST_search(root.left, target)
    else:
        return BST_search(root.right, target)


class node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __repr__(self):
        return f"node({self.item})"

def BST_min(root):
    if root.left:
        return BST_min(root.left)
    else:
        return root


def BST_max(root):
    if root.right:
        return BST_max(root.right)
    else:
        return root


def BST_successor(root):
    if root.right is not None:
        return BST_min(root.right)
    else:
        print("doesn't exists")


def BST_predeccessor(root):
    if root.left is not None:
        return BST_max(root.left)
    else:
        print("doesn't exists")


def BST_insert(root, item):
    if root is None:
        return node(item)
    if item <= root.item:
        root.left = BST_insert(root.left, item)
    else:
        root.right = BST_insert(root.right, item)
    return root


def BST_delete(root, item):
    if root is None:
        return None
    if item < root.item:
        root.left = BST_delete(root.left, item)
    elif item > root.item:
        root.right = BST_delete(root.right, item)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = BST_successor(root)
            root.item = successor.item
            root.right = BST_delete(root.right, successor.item)
    return root


def BST_to_sorted_arr(root):
    if root is None:
        return []
    return BST_to_sorted_arr(root.left) + [root.item] + BST_to_sorted_arr(root.right)


def ordinal(n):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    last_digit = n % 10
    if last_digit == 1:
        suffix = 'st'
    elif last_digit == 2:
        suffix = 'nd'
    elif last_digit == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    return f'{n}{suffix}'


def BST_to_reversed_sorted_arr(root):
    if root is None:
        return []
    return BST_to_reversed_sorted_arr(root.right) + [root.item] + BST_to_reversed_sorted_arr(root.left)


def BST_Kth_smallest(root, k):
    values = BST_to_sorted_arr(root)
    return values[k - 1]


def BST_Kth_largest(root, k):
    values = BST_to_reversed_sorted_arr(root)
    return values[k - 1]


def is_BST(root):
    def helper(root, min_val, max_val):
        if root is None:
            return True
        if not (min_val < root.item < max_val):
            return False
        return (helper(root.left, min_val, root.item) and helper(root.right, root.item, max_val))

    return helper(root, float('-inf'), float('inf'))


def BST_LCA(root, n1, n2):
    if root is None:
        return None
    if n1 < root.item and n2 < root.item:
        return BST_LCA(root.left, n1, n2)
    elif n1 > root.item and n2 > root.item:
        return BST_LCA(root.right, n1, n2)
    else:
        return root


def BST_closest_val(root, target):
    closest = root.item
    while root is not None:
        if abs(root.item - target) < abs(closest - target):
            closest = root.item
        if target < root.item:
            root = root.left
        elif target > root.item:
            root = root.right
        else:
            return root.item
    return closest


def are_BSTs_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.item != root2.item:
        return False
    return are_BSTs_identical(root1.left, root2.left) and are_BSTs_identical(root1.right, root2.right)


def sorted_arr_to_BST(arr):
    def helper(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = node(arr[mid])
        root.left, root.right = helper(start, mid - 1), helper(mid + 1, end)

    return helper(0, len(arr) - 1)


def BST_count_in_range(root, min_val, max_val):
    if root is None:
        return 0
    if root.item < min_val:
        return BST_count_in_range(root.right, min_val, max_val)
    elif root.item > max_val:
        return BST_count_in_range(root.left, min_val, max_val)
    else:
        return 1 + BST_count_in_range(root.left, min_val, max_val) + BST_count_in_range(root.right, min_val, max_val)



root = node(13)
root.left = node(11)
root.right = node(18)
root.left.left = node(7)
root.left.right = node(12)
root.right.left = node(15)
root.right.right = node(22)

root2 = node(13)
root2.left = node(11)
root2.right = node(18)
root2.left.left = node(7)
root2.left.right = node(12)
root2.right.left = node(15)
root2.right.right = node(22)

print(f'the height of the tree is {int(height(root))}')

if balancedTree(root):
    print("this tree is a balanced binarry tree")

if crockedTree(root):
    print("this tree is a crocked binarry tree")

if perfecTree(root):
    print("this tree is a perfect binarry tree")

print("Tree by levels:")
print_Tree_by_levels(root)

print(f'BST search result: {BST_search(root, root.left.left)}')

print(f'max value of the BST is: {BST_max(root)}')

print(f'min value of the BST is: {BST_min(root)}')

print(f'successor of the value of the BST root is: {BST_successor(root)}')

print(f'predeccessor of the value of the BST root is: {BST_predeccessor(root)}')

print(f'BST root after insertion: {BST_insert(root, 26)}')

print(f'BST root after deletion: {BST_delete(root, 26)}')

print(f'BST as a sorted array: {BST_to_sorted_arr(root)}')

print(f'BST as a reversed sorted array: {BST_to_reversed_sorted_arr(root)}')

print(f'LCA in a BST: {BST_LCA(root, 11, 18)}')

target = 6
print(f'closest value to {target} in the BST: {BST_closest_val(root, target)}')

k = 3
print(f'{ordinal(k)} smallest value in the BST: {BST_Kth_smallest(root, k)}')

print(f'{ordinal(k)} largest value in the BST: {BST_Kth_largest(root, k)}')

if is_BST(root):
    print("this tree is a binarry search tree")
else:
    print("this tree is not a binarry search tree")

if are_BSTs_identical(root, root2):
    print("those BSTs are the same")
else:
    print("those BSTs are different")

min_val = 7
max_val = 22
print(
    f'{BST_count_in_range(root, min_val, max_val)} nodes in the BST are both larger than {min_val} and smaller than {max_val}')


def binarrySearch(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid - 1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
goal = 3
result = binarrySearch(arr, goal)
if result != None:
    print(f'{goal} is in index {result}')
else:
    print(f'{goal} unfound in this array')