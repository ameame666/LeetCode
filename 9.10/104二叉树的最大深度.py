# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# 简简单单递归，时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点在递归中只被遍历一次。空间复杂度O(height)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1