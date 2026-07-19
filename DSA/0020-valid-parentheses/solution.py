class Solution:
    def isValid(self, s: str) -> bool:
        pCt = 0
        bCt = 0
        cCt = 0
        openStack = []

        for c in s:
            if c == "(":
                pCt += 1
                openStack.append("(")
            elif c == ")" and pCt > 0 and openStack[-1] == "(":
                pCt -= 1
                openStack.pop()
            elif c == "[":
                bCt += 1
                openStack.append("[")
            elif c == "]" and bCt > 0 and openStack[-1] == "[":
                bCt -= 1
                openStack.pop()
            elif c == "{":
                cCt += 1
                openStack.append("{")
            elif c == "}" and cCt > 0 and openStack[-1] == "{":
                cCt -= 1
                openStack.pop()
            else:
                return False

        if openStack:
            return False
        else:
            return True
