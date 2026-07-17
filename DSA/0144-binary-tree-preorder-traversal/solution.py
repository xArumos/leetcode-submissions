class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []

        if (root is not None):
            preorder.append(root.val)
        else:
            return preorder
        if (root.left is not None):
            preorder.extend(self.preorderTraversal(root.left))
        if (root.right is not None):
            preorder.extend(self.preorderTraversal(root.right))
        return preorder
