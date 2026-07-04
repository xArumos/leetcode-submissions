class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = 200
        minLengthIndex = 0
        result = ""

        if (len(strs) == 1):
            return strs[0]

        for i, string in enumerate(strs):
            if (len(string) == 0):
                return ""
            if (len(string) < minLength):
                minLength = len(string)
                minLengthIndex = i

        for l in range(minLength + 1):
            for string in strs:
                if (string[:l] != strs[minLengthIndex][:l]):
                    return result
            result = strs[minLengthIndex][:l]
        
        return result
