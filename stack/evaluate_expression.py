import re
from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def infix_to_postfix(self, tokens: List[str]) -> List[str]:
        operator_orders = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

        stack = []
        result = []

        for token in tokens:
            if token == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            elif token == "(":
                stack.append("(")
            elif token in operator_orders:
                while (
                    stack
                    and stack[-1] != "("
                    and operator_orders[stack[-1]] >= operator_orders[token]
                ):
                    result.append(stack.pop())

                stack.append(token)
            else:
                result.append(token)

        stack.reverse()
        result.extend(stack)
        return result

    def evaluate_postfix(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-/*^":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(a / b)
                elif token == "^":
                    stack.append(a**b)
            else:
                stack.append(float(token))

        return stack.pop()

    def solve(self, s: str) -> int:
        tokens = re.split(r"([()+\-/^*])", s)
        tokens = [token.strip() for token in tokens if token.strip()]

        postfix = self.infix_to_postfix(tokens)
        result = self.evaluate_postfix(postfix)

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve("1+2*(8-6/2)^2-5"))
