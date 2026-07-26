class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []

        for num in digits:
            if not result:
                for char in letterMap[num]:
                    result.append(char)
            else:
                letterCount = len(letterMap[num])
                resultSize = len(result)

                result *= letterCount
                for i, string in enumerate(result):
                    result[i] = string + (letterMap[num][i // resultSize])
        
        return result
