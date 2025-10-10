class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True
        if root.val == subRoot.val:
            if self.areSame(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def areSame(self, root1, root2):
        if not root1 or not root2:
            return not root1 and not root2
        return root1.val == root2.val and self.areSame(root1.left,root2.left) and self.areSame(root1.right,root2.right)
