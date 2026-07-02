class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if (compliment in visited and compliment + num == target):
                return [i, visited[compliment]]
            
            visited[num] = i



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, iNum in enumerate(nums):
#             for j, jNum in enumerate(nums):
#                 if (i != j and iNum + jNum == target):
#                     return [i, j]
