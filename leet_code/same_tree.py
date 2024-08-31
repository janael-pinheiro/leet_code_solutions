from typing import Optional

from leet_code.maximum_depth_of_binary_tree import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    p_queue = [p]
    q_queue = [q]
    while len(p_queue) > 0 and len(q_queue) > 0:
        p_current = p_queue.pop(0)
        q_current = q_queue.pop(0)
        if (p_current is None and q_current is not None) or (p_current is not None and q_current is None):
            return False
        elif p_current is None and q_current is None:
            continue
        if p_current.val != q_current.val:
            return False
        p_queue.append(p_current.left)
        p_queue.append(p_current.right)
        q_queue.append(q_current.left)
        q_queue.append(q_current.right)
    if len([x for x in p_queue if x is not None]) == 0 and len([x for x in q_queue if x is not None]) == 0:
        return True
    return False

