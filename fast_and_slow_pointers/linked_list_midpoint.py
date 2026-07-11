class ListNode:
    def __init__(self, val: int, next: ListNode | None = None) -> None:
        self.val = val
        self.next = ListNode


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, root: ListNode) -> ListNode | None:
        slow = fast = root

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
