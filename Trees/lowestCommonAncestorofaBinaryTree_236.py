class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return 
        if root.val == p.val or root.val == q.val:
            return root
        llca = self.lowestCommonAncestor(root.left,p,q)
        rlca = self.lowestCommonAncestor(root.right,p,q)
        if llca and rlca:
            return root
        return llca if llca else rlca