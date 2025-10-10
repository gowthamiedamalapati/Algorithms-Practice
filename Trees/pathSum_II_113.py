class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return []
        paths = []
        path = []
        self.utility(root,targetSum,paths,path)
        return paths

    def utility(self,root,sum,paths,path):
        if not root:
            return
        if not root.left and not root.right and sum == root.val:
            path.append(root.val)
            paths.append(path[:])
            path.pop()
            return
        path.append(root.val)
        self.utility(root.left,sum-root.val,paths,path)
        self.utility(root.right,sum-root.val,paths,path)
        path.pop()
        return
