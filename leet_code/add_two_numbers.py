from typing import Optional

from leet_code.nodes import ListNode


def convert_linked_list_to_integer(head: Optional[ListNode], multiplier):
    if head is None:
        return 0
    value = convert_linked_list_to_integer(head.next, multiplier * 10)
    return value + head.val * multiplier


def convert_integer_to_linked_list(value: int) -> Optional[ListNode]:
    if value // 10 == 0:
        return ListNode(value)
    next_node = convert_integer_to_linked_list(value // 10)
    current_node = ListNode(value % 10)
    current_node.next = next_node
    return current_node


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    first_integer = convert_linked_list_to_integer(l1, 1)
    second_integer = convert_linked_list_to_integer(l2, 1)
    result = first_integer + second_integer
    return convert_integer_to_linked_list(result)
