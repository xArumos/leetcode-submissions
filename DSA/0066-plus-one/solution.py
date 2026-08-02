class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits

        for i, num in enumerate(reversed(result)):
            comp = len(result) - i - 1
            if num < 9:
                result[comp] = result[comp] + 1
                break
            else:
                result[comp] = result[comp] + 1
                result[comp] = result[comp] % 10
                if comp == 0:
                    result.insert(0, 1)

        return result
