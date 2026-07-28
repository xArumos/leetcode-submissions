class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftIndex = 0
        rightIndex = max(len(height) - 1, 0)
        maxArea = 0

        while leftIndex != rightIndex:
            area = (rightIndex - leftIndex) * min(height[leftIndex], height[rightIndex])
            maxArea = max(maxArea, area)
            if height[leftIndex] > height[rightIndex]:
                rightIndex -= 1
            elif height[leftIndex] <= height[rightIndex]:
                leftIndex += 1
        return maxArea
