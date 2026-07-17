class Solution:
    class TreeNode:
        def __init__(self, val, left, right, openedCount, closedCount):
            self.val = val
            self.left = left
            self.right = right
            self.openedCount = openedCount
            self.closedCount = closedCount
    def buildTree(self, root, n):
        if root.openedCount < n:
            root.left = self.TreeNode(root.val + "(", None, None, root.openedCount + 1, root.closedCount)
            self.buildTree(root.left, n)
        if (root.closedCount < root.openedCount and root.closedCount < n):
            root.right = self.TreeNode(root.val + ")", None, None, root.openedCount, root.closedCount + 1)
            self.buildTree(root.right, n)
    def getLeafs(self, root) -> List[str]:
        result = []

        if root.left is None and root.right is None:
            result.append(root.val)
        if root.left is not None:
            result.extend(self.getLeafs(root.left))
        if root.right is not None:
            result.extend(self.getLeafs(root.right))
        return result
    def generateParenthesis(self, n: int) -> List[str]:
        root = self.TreeNode("(", None, None, 1, 0)
        self.buildTree(root, n)

        result = self.getLeafs(root)
        return result
