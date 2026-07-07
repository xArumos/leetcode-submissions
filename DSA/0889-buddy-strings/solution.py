class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        index1 = -1
        index2 = -1
        charCount = {}
        for i in range(len(s)):
            if s == goal:
                if s[i] in charCount:
                    return True
                else:
                    charCount[s[i]] = 1
            else:
                if s[i] != goal[i]:
                    if index1 == -1:
                        index1 = i
                    elif index2 == -1:
                        index2 = i
                    else:
                        return False
        
        if s == goal:
            return False
        if s[index1] == goal[index2] and s[index2] == goal[index1]:
            return True
        else:
            return False
