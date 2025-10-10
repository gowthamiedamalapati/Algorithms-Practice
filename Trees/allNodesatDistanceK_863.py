class Solution(object):
    def distanceK(self, root, target, k):

        def markParents(root,parent,target):
            q = deque()
            q.append(root)
            parent[root] = None
            temp = None
            while q:
                curr = q.popleft()
                # print(curr.val, type(curr.val), target, type(target))
                if curr == target:
                    temp = curr
                if curr.left:
                    q.append(curr.left)
                    parent[curr.left] = curr
                if curr.right:
                    q.append(curr.right)
                    parent[curr.right] = curr
            return temp
        def nodesatKDistance(targetNode,res,parent):
            seen = set()
            q = deque()
            q.append((targetNode,0))
            seen.add(targetNode.val)
            while q:
                curr,d = q.popleft()
                if d == k:
                    res.append(curr.val)
                elif d > k:
                    return 
                if curr.left and curr.left.val not in seen:
                    q.append((curr.left,d+1))
                    seen.add(curr.left.val)
                if curr.right and curr.right.val not in seen:
                    q.append((curr.right,d+1))
                    seen.add(curr.right.val)
                if parent[curr] and parent[curr].val not in seen:
                    q.append((parent[curr],d+1))
                    seen.add(parent[curr].val)
            return


        parent = {}
        targetNode = markParents(root,parent,target)
        print(targetNode)
        res = []
        if targetNode:
          nodesatKDistance(targetNode,res,parent)
        return res