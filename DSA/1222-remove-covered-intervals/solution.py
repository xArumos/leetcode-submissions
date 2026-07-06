class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        result = 0

        for i in intervals:
            covered = False

            for j in intervals:
                if (i != j and j[0] <= i[0] and i[1] <= j[1]):
                    covered = True
            if (covered):
                result += 1

        return (len(intervals) - result)
