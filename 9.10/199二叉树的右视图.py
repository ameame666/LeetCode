# https://leetcode.cn/problems/binary-tree-right-side-view/description/
# 层序遍历把每一层的节点加入列表，然后把每个列表的最后一个节点的值加入结果，时间复杂度O(n)，最坏空间复杂度O(n)
# bfs
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            nxt =  []
            res.append(cur[-1].val)
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
        
        return res

# dfs可以将空间复杂度降到O(k)，但最坏还是O(k)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        res = []
        dfs(root, 0)
        return res