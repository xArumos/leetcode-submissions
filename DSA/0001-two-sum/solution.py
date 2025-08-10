class Solution(object):
    def twoSum(self, nums, target):
        for i, j in enumerate(nums):
            for k, l in enumerate(nums):
                if i == k:
                    pass
                else:
                    if j + l == target:
                        return [i, k]
        return []
