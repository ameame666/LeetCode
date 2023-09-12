# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 注意两点，第一点是判断是否越界，也就是prestart > preeend，此外建立字典存储中序存储从值到索引的映射，只需要确定每次的左侧长度以及右侧长度就能确定每次传入的参数
# 时间复杂度O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}
        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i
        
        def build(prestart, preend, instart, inend):
            if prestart > preend:
                return 
            rootval = preorder[prestart]
            root = TreeNode(rootval)
            index = inorder_index[rootval]
            leftlength = index - instart
            rightlength = inend - index + 1

            root.left = build(prestart+1, prestart+leftlength, instart, index-1)
            root.right = build(prestart+leftlength+1, preend, index+1, inend)
            return root
        
        return build(0, len(preorder)-1, 0, len(inorder)-1)