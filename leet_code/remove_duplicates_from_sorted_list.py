from leet_code.nodes import ListNode
from typing import Optional


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    current = head
    while current is not None and current.next is not None:
        next_node = current.next
        while next_node is not None and current.val == next_node.val:
            next_node = next_node.next
        current.next = next_node
        current = current.next
    return head
