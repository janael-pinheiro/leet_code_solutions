from leet_code.nodes import ListNode

from typing import Optional, Tuple


def _reverse(head: Optional[ListNode]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    if head.next is None:
        return head, head
    current, new_head = _reverse(head.next)
    head.next = None
    current.next = head
    return head, new_head


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    _, new_head = _reverse(head)
    return new_head
