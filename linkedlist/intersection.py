class ListNode:
    def __init__(self, val: int, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        pass

    def intersection(self, root1: ListNode, root2: ListNode) -> ListNode | None:
        ptr1, ptr2 = root1, root2

        while ptr1 != ptr2:
            ptr1 = ptr1.next if ptr1 else root2
            ptr2 = ptr2.next if ptr2 else root1

        return ptr1
