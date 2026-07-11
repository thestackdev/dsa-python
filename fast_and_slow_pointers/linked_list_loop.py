class ListNode:
    def __init__(self, val: int, next: ListNode | None = None) -> None:
        self.val = val
        self.next = ListNode


class Solution:
    def __init__(self) -> None:
        pass

    def solution(self, root) -> bool:
        slow = root
        fast = root

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
