class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        balanced = self.utility(root)
        return True if balanced > -1 else False
        
    def utility(self,root):
        if not root:
            return 0
        left = self.utility(root.left)
        right = self.utility(root.right)
        if (left == -1 or right == -1) or (left == -1 and right == -1) :
            return -1
        if abs(right-left)>=2:
            return -1
        return 1+max(left,right)
        