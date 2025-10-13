class Solution(object):
    def findCenter(self, edges):
        map = defaultdict(list)
        seen = set()
        for edge in edges:
            map[edge[0]].append(edge[1])
            map[edge[1]].append(edge[0])
        for key, value in map.items():
            if len(value) == len(edges) :
                return key
        return -1
        