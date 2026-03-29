class linked_list_node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.random = None
        self.down = None
        self.mirror = None

    def __repr__(self):
        return f'linked_list_node({self.item})'

class node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __repr__(self):
        return f"node({self.item})"


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.item, end="》")
        current = current.next
    print("None")


def linked_list_delete(head, target):
    if head is None:
        return None
    if head.item == target:
        return head.next
    previous = head
    current = head.next
    while current is not None:
        if current.item == target:
            previous.next = current.next
            return head
        previous = current
        current = current.next
    return head


def linked_list_is_cycle(head):
    turtle = rabbit = head
    while rabbit is not None and rabbit.next is not None:
        turtle = turtle.next
        rabbit = rabbit.next.next
        if turtle == rabbit:
            return True
    return False


def linked_list_cycle_start(head):
    appeared = set()
    current = head
    while current is not None:
        if current in appeared:
            return current
        appeared.add(current)
        current = current.next
    return None


def reverse_linked_list(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


def linked_lists_common_node(head1, head2):
    p1, p2 = head1, head2
    while p1 != p2:
        if p1 is not None:
            p1 = p1.next
        else:
            p1 = head2
        if p2 is not None:
            p2 = p2.next
        else:
            p2 = head1
    return p1


def linked_list_mid(head):
    turtle = rabbit = head
    while rabbit and rabbit.next:
        rabbit = rabbit.next.next
        turtle = turtle.next
    return turtle


def is_linked_list_odd(head):
    current = head
    count = 0
    while current is not None:
        count += 1
        current = current.next
    if count % 2 != 0:
        return True
    else:
        return False


def merge_sorted_linked_lists(head1, head2):
    temp = linked_list_node(0)
    current = temp
    while head1 is not None and head2 is not None:
        if head1.item < head2.item:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    if head1 is None:
        current.next = head2
    else:
        current.next = head1
    return temp.next


def is_linked_list_palindrom(head):
    if head is None or head.next is None:
        return True
    mid = linked_list_mid(head)
    if is_linked_list_odd(head):
        mid = mid.next
    prev_mid = None
    current = head
    while current is not mid:
        prev_mid = current
        current = current.next
    first_half, second_half = head, reverse_linked_list(mid)
    while first_half is not mid and second_half is not None:
        if first_half.item != second_half.item:
            prev_mid.next = reverse_linked_list(mid)
            return False
        first_half, second_half = first_half.next, second_half.next
    prev_mid.next = reverse_linked_list(mid)
    return True


def merge_k_sorted_linked_lists(*heads):
    pointers = list(heads)
    temp = linked_list_node(0)
    current = temp
    while any(pointers):
        for i, node in enumerate(pointers):
            if node is not None:
                min_node = node
                min_index = i
                break
        for i, node in enumerate(pointers):
            if node is not None and node.item < min_node.item:
                min_node = node
                min_index = i
        current.next = min_node
        pointers[min_index] = pointers[min_index].next
        current = current.next
    return temp.next


def linked_list_merge_sort(head):
    if head is None or head.next is None:
        return head
    mid = linked_list_mid(head)
    prev_mid = None
    current = head
    while current is not mid:
        prev_mid = current
        current = current.next
    if prev_mid is not None:
        prev_mid.next = None
    left_sorted_list, right_sorted_list = linked_list_merge_sort(head), linked_list_merge_sort(mid)
    sorted_list = merge_sorted_linked_lists(left_sorted_list, right_sorted_list)
    return sorted_list

def sorted_linked_list_to_BST(head):
    if head is None:
        return None
    mid = linked_list_mid(head)
    prev_mid, current = None, head
    while current is not mid:
        prev_mid = current
        current = current.next
    root = node(mid.item)
    left_list, right_list = head, mid.next
    if prev_mid is not None:
        prev_mid.next = None
    else:
        left_list = None
    mid.next = None
    root.left, root.right = sorted_linked_list_to_BST(left_list), sorted_linked_list_to_BST(right_list)
    return root

def linked_list_remove_duplicates(head):
    current = head
    check = set()
    previous = None
    while current is not None:
        if current.item in check:
            previous.next = current.next
        else:
            check.add(current.item)
            previous = current
        current = current.next
    return head


def linked_list_evens_and_odds(head):
    even_head, odd_head = linked_list_node(0), linked_list_node(float('inf'))
    current = head
    even_curr, odd_curr = even_head, odd_head
    while current is not None:
        if current.item % 2 == 0:
            even_curr.next = current
            even_curr = even_curr.next
        else:
            odd_curr.next = current
            odd_curr = odd_curr.next
        current = current.next
    even_curr.next = odd_curr.next = None
    return even_head.next, odd_head.next


def linked_list_swap_pairs(head):
    temp = linked_list_node(0)
    current, curr_temp = head, temp
    while current is not None and current.next is not None:
        next_curr = current.next.next
        curr_temp.next = current.next
        curr_temp.next.next = current
        current.next = None
        current = next_curr
        curr_temp = curr_temp.next.next
    if current is not None:
        curr_temp.next = current
    return temp.next


def linked_list_fold(head):
    if head is None or head.next is None:
        return head
    temp = linked_list_node(0)
    current = temp
    mid = linked_list_mid(head)
    prev_mid, curr = None, head
    while curr is not mid:
        prev_mid = curr
        curr = curr.next
    prev_mid.next = None
    first_half, second_half = head, reverse_linked_list(mid)
    while first_half and second_half:
        first_next = first_half.next
        current.next = first_half
        current.next.next = second_half
        current = current.next.next
        first_half, second_half = first_next, second_half.next
    if second_half is not None:
        current.next = second_half
    return temp.next


def linked_list_to_number(head):
    count = 0
    current = head
    while current is not None:
        count = count * 10 + current.item
        current = current.next
    return count


def number_to_linked_list(num):
    num = str(num)
    tmp = linked_list_node(0)
    current = tmp
    for digit in num:
        current.next = linked_list_node(int(digit))
        current = current.next
    return tmp.next


def clone_linked_list_with_random(head):
    if head is None:
        return None
    current = head
    while current is not None:
        next_curr = current.next
        current.next = linked_list_node(current.item)
        current.next.next = next_curr
        current = next_curr
    current2 = head
    while current2 is not None:
        if current2.random is not None:
            current2.next.random = current2.random.next
        current2 = current2.next.next
    temp = linked_list_node(0)
    current3, curr_temp = head, temp
    while current3 is not None:
        clone = current3.next
        curr_temp.next = clone
        current3.next = clone.next
        current3 = current3.next
        curr_temp = curr_temp.next
    return temp.next


def clone_linked_list_with_sublists(head):
    if head is None:
        return head

    def clone_nodes(head):
        current = head
        while current is not None:
            next_curr = current.next
            current.next = linked_list_node(current.item)
            current.next.next = next_curr
            if current.down is not None:
                clone_nodes(current.down)
            current = next_curr
        return head

    def connect_clones_with_subclones(head):
        current = head
        while current is not None:
            if current.down is not None:
                current.next.down = current.down
                connect_clones_with_subclones(current.down)
            current = current.next.next
        return head

    def separate_clones(head):
        temp = linked_list_node(0)
        current, curr_temp = head, temp
        while current is not None:
            clone = current.next
            current.next = clone.next
            curr_temp.next = clone
            if clone.down is not None:
                clone.down = separate_clones(clone.down)
            current = current.next
            curr_temp = curr_temp.next
        return temp.next

    step1 = clone_nodes(head)
    step2 = connect_clones_with_subclones(step1)
    step3 = separate_clones(step2)
    return step3


def clone_linked_list_with_mirror(head):
    if head is None:
        return None

    def clone_list(head):
        temp, current = linked_list_node(0), head
        curr_temp = temp
        while current is not None:
            curr_temp.next = linked_list_node(current.item)
            current, curr_temp = current.next, curr_temp.next
        return temp.next

    clone = clone_list(head)
    mid = linked_list_mid(clone)
    if is_linked_list_odd(clone):
        mid.mirror = mid
        first, second = clone, reverse_linked_list(mid.next)
        mid.next = None
        while first is not mid and second:
            first.mirror, second.mirror = second, first
            first, second = first.next, second.next
        mid.next = reverse_linked_list(second)
    else:
        first, second = clone, reverse_linked_list(mid)
        curr, prev_mid = clone, None
        while curr is not mid:
            prev_mid, curr = curr, curr.next
        prev_mid.next = None
        while first and second:
            first.mirror, second.mirror = second, first
            first, second = first.next, second.next
        prev_mid.next = reverse_linked_list(second)
    return clone


common = linked_list_node(18)

head = linked_list_node(1)
head.next = linked_list_node(2)
head.next.next = linked_list_node(3)
head.next.next.next = linked_list_node(4)
head.next.next.next.next = linked_list_node(5)
head.next.next.next.next.next = linked_list_node(6)
head.next.next.next.next.next.next = linked_list_node(17)

head2 = linked_list_node(8)
head2.next = linked_list_node(9)
head2.next.next = common

head3 = linked_list_node(10)
head3.next = linked_list_node(11)
head3.next.next = linked_list_node(12)
head3.next.next.next = linked_list_node(13)

head4 = linked_list_node(14)
head4.next = linked_list_node(15)
head4.next.next = linked_list_node(16)

head5 = linked_list_node(1)
head5.next = linked_list_node(2)
head5.next.next = linked_list_node(3)

head6 = linked_list_node(21)
head6.next = linked_list_node(22)
head6.next.next = linked_list_node(23)
head6.next.next.next = linked_list_node(24)

head7 = linked_list_node(25)
head7.next = linked_list_node(26)
head7.next.next = linked_list_node(27)

head8 = linked_list_node(4)
head8.next = linked_list_node(13)
head8.next.next = linked_list_node(9)
head8.next.next.next = linked_list_node(2)
head8.next.next.next.next = linked_list_node(17)

head9 = linked_list_node(4)
head9.next = linked_list_node(19)
head9.next.next = linked_list_node(7)
head9.next.next.next = linked_list_node(4)
head9.next.next.next.next = linked_list_node(19)
head9.next.next.next.next.next = linked_list_node(7)

head10 = linked_list_node(31)
head10.next = linked_list_node(32)
head10.next.next = linked_list_node(33)
head10.next.next.next = linked_list_node(34)
head10.next.next.next.next = linked_list_node(35)
head10.next.next.next.next.next = linked_list_node(36)
head10.next.next.next.next.next.next = linked_list_node(37)
head10.next.next.next.next.next.next.next = linked_list_node(38)

head11 = linked_list_node(91)
head11.next = linked_list_node(2)
head11.next.next = linked_list_node(34)
head11.next.next.next = linked_list_node(65)
head11.next.next.next.next = linked_list_node(17)
head11.next.next.next.next.next = linked_list_node(79)
head11.next.next.next.next.next.next = linked_list_node(6)
head11.next.next.next.next.next.next.next = linked_list_node(22)

if linked_list_is_cycle(head3):
    print("there is a cycle in the linked list")
else:
    print("there isn't a cycle in the linked list")

print(f'first common node in both of the linked lists: {linked_lists_common_node(head, head2)}')

print(f'mid of the linked_list: {linked_list_mid(head)}')

print(f'linked list start of the cycle: {linked_list_cycle_start(head3)}')

merged = merge_sorted_linked_lists(head3, head4)
print(f'merged linked list:')
print_linked_list(merged)

if is_linked_list_palindrom(head5):
    print("this linked list is a palindrom")
else:
    print("this linked list is not a palindrom")

print("merged sorted linked list:")
merged2 = merge_k_sorted_linked_lists(head5, head6, head7)
print_linked_list(merged2)

print("sorted linked list:")
sorted_head8 = linked_list_merge_sort(head8)
print_linked_list(sorted_head8)

root_of_list = sorted_linked_list_to_BST(sorted_head8)

head9_no_dups = linked_list_remove_duplicates(head9)
print("linked list after removing duplicates")
print_linked_list(head9_no_dups)

even_head10, odd_head10 = linked_list_evens_and_odds(head10)
print("list of only evens nodes in the list:")
print_linked_list(even_head10)
print("list of only odds nodes in the list:")
print_linked_list(odd_head10)

print("zigzag linked list:")
fold_head11 = linked_list_fold(head11)
print_linked_list(fold_head11)

print("linked list after swaping adjacent pairs of nodes:")
swaped_head11 = linked_list_swap_pairs(head11)
print_linked_list(swaped_head11)

print(f'linked list as a number: {linked_list_to_number(head11)}')
head12 = number_to_linked_list(109734)
print(f'number as a linked list:')
print_linked_list(head12)