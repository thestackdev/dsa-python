from operator import ne
from typing import Generator


class ListNode:
    def __init__(self, val: int, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, val: int) -> None:
        node = ListNode(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def push_back(self, val: int) -> None:
        node = ListNode(val)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def __iter__(self) -> Generator[int]:
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next


if __name__ == "__main__":
    solution = LinkedList()

    solution.push_back(10)
    solution.push_back(20)
    solution.push_back(30)
    solution.push_back(40)

    for val in solution:
        print(val)
