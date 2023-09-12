# https://leetcode.cn/problems/invert-binary-tree/
# 先交换左右节点，然后调用函数交换左右子树，时间复杂度O(n)，空间复杂度O(h)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root