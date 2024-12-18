from typing import Optional

from leet_code.nodes import ListNode


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == right:
        return head
    previous_left = None
    current = head
    last = head
    left_node = head
    right_node = head
    index = 1
    last = None
    while index <= right:
        temp = current.next
        if index == left and left != 1:
            previous_left = last
            left_node = current
        elif index == left and left == 1:
            left_node = current
        elif index == right:
            right_node = current
            index += 1
            continue
        else:
            if right - left > 1 and left < index < right:
                current.next = last
        last = current
        current = temp
        index += 1

    if previous_left is not None:
        previous_left.next = right_node
        left_node.next = right_node.next
        right_node.next = last
    elif previous_left is None and right_node.next is None and right - left == 1:
        left_node.next = right_node.next
        right_node.next = left_node
        head = right_node
    elif previous_left is None and right - left != 1:
        left_node.next = right_node.next
        right_node.next = last
        head = right_node
    elif previous_left is None and right - left == 1:
        left_node.next = right_node.next
        right_node.next = left_node
        head = right_node
    return head
