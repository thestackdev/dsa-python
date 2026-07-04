from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def solve(self, s: str) -> List[str]:
        result = []
        self.backtrack(s, s, 0, result)
        return result

    def backtrack(
        self, s: str, candidate: str, current_index: int, result: List[str]
    ) -> None:

        if len(s) == current_index:
            result.append(candidate)
            return

        if candidate[current_index].isalpha():
            self.backtrack(
                s,
                candidate[:current_index]
                + candidate[current_index].upper()
                + candidate[current_index + 1 :],
                current_index + 1,
                result,
            )

            self.backtrack(
                s,
                candidate[:current_index]
                + candidate[current_index].lower()
                + candidate[current_index + 1 :],
                current_index + 1,
                result,
            )

        else:
            self.backtrack(s, candidate, current_index + 1, result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve("a1b2"))
