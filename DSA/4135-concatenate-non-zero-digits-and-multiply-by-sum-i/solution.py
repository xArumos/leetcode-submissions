class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp = n
        xString = ""

        if n == 0:
            return 0

        while temp != 0:
            digit = temp % 10
            if digit == 0:
                temp = temp // 10
            else:
                temp = temp // 10
                xString = str(digit) + xString

        x = 0

        for char in xString:
            x += int(char)

        return x * int(xString)
