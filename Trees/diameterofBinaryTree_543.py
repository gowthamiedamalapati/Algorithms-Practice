class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        self.utility(root,res)
        return res[0]

    def utility(self,root,res):
        if not root:
            return 0
        left = self.utility(root.left,res)
        right = self.utility(root.right,res)
        res[0] = max(res[0],left+right)
        return 1+max(left,right)
        