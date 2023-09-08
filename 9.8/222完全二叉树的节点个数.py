# 层序遍历数节点，时间复杂度是O(n)，空间复杂度O(logn)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        cur = [root]
        while cur:
            count += len(cur)
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
        
        return count
    
# 用递归的方法来实现，先判断是不是完全二叉树，是的话直接计算，不是的话用递归计算
# 时间复杂度O(log^2(n))，空间复杂度O(logn)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftheight, rightheight = 0, 0
        left, right = root, root
        while left:
            left = left.left
            leftheight += 1
        while right:
            right = right.right
            rightheight += 1
        if leftheight == rightheight:
            return  2 ** leftheight - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)