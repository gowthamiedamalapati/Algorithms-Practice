class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        q = deque()
        q.append((root,0))
        res = {}
        ans = []
        while q:
            curr,d = q.popleft()
            if d not in res:
                res[d] = curr.val
                ans.append(curr.val)
            if curr.right:
                q.append((curr.right,d+1))
            if curr.left:
                q.append((curr.left,d+1))
        return ans