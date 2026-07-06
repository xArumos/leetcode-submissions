class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = "aeiou"
        result = s

        if (not s):
            return ""

        while (result[-1] in vowels):
            result = result[:-1]
            if (not result):
                break

        return result
