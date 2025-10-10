class Solution(object):
    def flatten(self, root):
        if not root:
           return
        stack  = []
        curr = root
        while curr:
            if curr.right:
               stack.append(curr.right)
            if curr.left:
               curr.right = curr.left
            elif stack:
                curr.right = stack.pop()
            else:
                curr.right = None
            curr.left = None
            curr = curr.right
        return root
