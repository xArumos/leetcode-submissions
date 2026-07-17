class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        if p.left is not None and q.left is not None:
            if not self.isSameTree(p.left, q.left):
                return False
        elif (p.left is None and q.left is not None) or (p.left is not None and q.left is None):
            return False
        if p.right is not None and q.right is not None:
            if not self.isSameTree(p.right, q.right):
                return False
        elif (p.right is None and q.right is not None) or (p.right is not None and q.right is None):
            return False
        return True
