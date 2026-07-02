class Solution:
    def isPalindrome(self, x: int) -> bool:
        converted = str(x)

        print(converted[0:(len(converted) // 2)])
        print(converted[(len(converted) // 2):])

        if (len(converted) % 2 == 0):
            if (converted[0:(len(converted) // 2)] == converted[(len(converted) // 2):][::-1]):
                return True
            else:
                return False
        else:
            if (converted[0:(len(converted) // 2)] == converted[(len(converted) // 2 + 1):][::-1]):
                return True
            else:
                return False
