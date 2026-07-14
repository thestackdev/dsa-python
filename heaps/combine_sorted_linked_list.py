import heapq
from typing import Any, List, Self


class Node:
    def __init__(self, val: int, next: Self | None = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

    def __lt__(self, other: Self) -> bool:
        return self.val < other.val


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, heads: List[Node]):
        heap = []

        for head in heads:
            heapq.heappush(heap, head)

        dummy = Node(0)
        node = dummy

        while heap:
            smallest = heapq.heappop(heap)
            node.next = smallest
            if smallest.next:
                heapq.heappush(heap, smallest.next)
            node = smallest

        node.next = None
        return dummy.next


def build_list(values: List[int]) -> Node | None:
    """Build a linked list from a Python list, return its head."""
    head = None
    prev = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
        else:
            prev.next = node
        prev = node
    return head


if __name__ == "__main__":
    heads = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6]),
    ]
    solution = Solution()
    solution.solve(heads)
