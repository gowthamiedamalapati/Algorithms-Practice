class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        path = []

        def backtrack(node):
            if not node:
                return
            if not node.left and not node.right:
                path.append(str(node.val))
                ans = "->".join(path)
                path.pop()
                res.append(ans)
                print(res)
                return
            path.append(str(node.val))
            backtrack(node.left)
            backtrack(node.right)
            path.pop()
            return
     
        backtrack(root)
        return res