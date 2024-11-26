from typing import Optional, Tuple

from leet_code.nodes import ListNode


def _delete(head: Optional[ListNode], index: int) -> Tuple[Optional[ListNode], int]:
    if head is None:
        return head, index
    next_node, count = _delete(head.next, index + 1)
    if count // 2 == index:
        head.next = None
        return next_node, count
    head.next = next_node
    return head, count


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    head, _ = _delete(head, 0)
    return head
