class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        cycle = set()
        visit = set()
        def dfs(u):
            if u in cycle: return False
            if u in visit: return True
            cycle.add(u)
            for p in adj[u]:
                if not dfs(p): return False
            cycle.remove(u)
            visit.add(u)
            res.append(u)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return res
            