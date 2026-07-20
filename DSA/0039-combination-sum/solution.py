class Solution:
    class TreeNode:
        def __init__(self, val, diffs):
            self.val = val
            self.diffs = diffs
            self.children = []
    def buildTree(self, root, candidates):
        if root.val == 0:
            if root.diffs not in self.result:
                self.result.append(root.diffs)
        else:
            for num in candidates:
                if root.val >= num:
                    copy = root.diffs + [num]
                    copy.sort()
                    root.children.append(self.TreeNode(root.val - num, copy))
            for node in root.children:
                self.buildTree(node, candidates)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        root = self.TreeNode(target, [])

        self.buildTree(root, candidates)

        return self.result
