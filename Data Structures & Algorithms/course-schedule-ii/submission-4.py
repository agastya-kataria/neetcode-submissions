class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        visited = set()
        visiting = set()
        def dfs(u):
            if u in visiting: return False
            if u in visited: return True
            visiting.add(u)
            for nei in adj[u]:
                if not dfs(nei): return False
            
            visiting.remove(u)
            visited.add(u)
            adj[u] = []
            res.append(u)
            return True
        
        for n in range(numCourses):
            if not dfs(n): return []
        return res
                    
