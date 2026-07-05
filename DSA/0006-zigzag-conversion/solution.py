class Solution:
    def convert(self, s: str, numRows: int) -> str:
        layers = []
        index = 0
        reverse = True
        height = 0

        if (numRows == 1):
            return s
        for i in range(numRows):
            layers.append([])



        while (index != len(s)):
            if (height == numRows - 1 or height == 0):
                reverse = not reverse
            layers[height].append(s[index])
            index += 1
            if (not reverse):
                height += 1
            else:
                height -= 1
        result = ""
        for arr in layers:
            for char in arr:
                result += char
        
        return result
