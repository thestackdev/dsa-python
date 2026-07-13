class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, s: str) -> bool:
        stack = []

        close_braces = {"]": "[", "}": "{", ")": "("}

        for ch in s:
            if ch in close_braces:
                if not stack or close_braces.get(ch) != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve("([]{})"))
