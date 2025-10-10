class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.ismirror(root.left,root.right)

    def ismirror(self,p,q):
        if not p and not q:
            return True
        elif (not p or not q) or (p.val != q.val):
            return False
        return self.ismirror(p.left,q.right) and self.ismirror(p.right,q.left)