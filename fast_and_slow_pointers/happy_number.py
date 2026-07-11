class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, n: int) -> bool:
        slow = fast = n

        while True:
            slow = self.get_next_number(slow)
            fast = self.get_next_number(self.get_next_number(fast))

            if fast == 1:
                return True

            elif slow == fast:
                return False

    def get_next_number(self, n: int) -> int:
        next_digit = 0

        while n > 0:
            rem = n % 10
            n //= 10
            next_digit += rem**2

        return next_digit
