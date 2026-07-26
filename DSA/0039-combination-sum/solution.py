class Solution:
    def combinationSum(self, candidates, target):
        result = []
        path = []

        def dfs(remain, start):
            if remain == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remain:
                    continue
                path.append(num)
                dfs(remain - num, i)
                path.pop()
            
        dfs(target, 0)
        return result
