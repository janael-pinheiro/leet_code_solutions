from leet_code.nodes import ListNode
from typing import Optional, Tuple


def get_next_node(current1: ListNode, current2: ListNode, next_node: ListNode) -> Tuple[ListNode, ListNode, ListNode]:
    if current1.val < current2.val:
        next_node.next = ListNode(current1.val)
        current1 = current1.next
    elif current1.val > current2.val:
        next_node.next = ListNode(current2.val)
        current2 = current2.next
    else:
        next_node.next = ListNode(current1.val)
        current1 = current1.next
        current2 = current2
    return next_node.next, current1, current2


def get_head_node(list1: ListNode, list2: ListNode) -> Tuple[ListNode, ListNode, ListNode]:
    head = None
    current1 = None
    current2 = None
    if list1.val < list2.val:
        head = ListNode(list1.val)
        current1 = list1.next
        current2 = list2
    elif list1.val > list2.val:
        head = ListNode(list2.val)
        current1 = list1
        current2 = list2.next
    else:
        head = ListNode(list1.val)
        current1 = list1.next
        current2 = list2
    return head, current1, current2


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None and list2 is None:
        return None
    elif list1 is None and list2 is not None:
        return list2
    elif list1 is not None and list2 is None:
        return list1
    head, current1, current2 = get_head_node(list1, list2)
    next_node = head
    while current1 is not None and current2 is not None:
        next_node, current1, current2 = get_next_node(current1, current2, next_node)
    if current1 is None:
        while current2 is not None:
            next_node.next = current2
            next_node = next_node.next
            current2 = current2.next
    if current2 is None:
        while current1 is not None:
            next_node.next = current1
            next_node = next_node.next
            current1 = current1.next
    return head
