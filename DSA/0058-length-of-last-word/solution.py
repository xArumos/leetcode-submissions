class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = False
        count = 0
        for i, char in enumerate(reversed(s)):
            if (char == " " and word):
                return count
            elif (char != " "):
                count += 1
                word = True
        
        return count
