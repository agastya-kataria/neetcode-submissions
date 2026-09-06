class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        visit = set()
        
        def dfs(c):
            if c in visit: return False
            if adj[c] == []: return True
            visit.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visit.remove(c)
            adj[c] = []
            return True
        
        for a, b in prerequisites:
            if not dfs(a): return False
        
        return True