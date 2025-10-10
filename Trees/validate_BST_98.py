class Solution(object):
    def isValidBST(self, root):
        return self.utility(root,[float('-inf')])
    
    def utility(self,root,prev):
        if not root:
            return True
        if not self.utility(root.left,prev):
            return False
        if root.val <= prev[0]:
            return False
        prev[0] = root.val
        return self.utility(root.right,prev)
    

    #ex [2,2,2] also returns False because we are checking strictly smaller and strictly greater in BST