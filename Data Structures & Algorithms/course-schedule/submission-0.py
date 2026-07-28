class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap ={i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        visitSet = set()
        def dfs(c):
            if c in visitSet: return False
            if preMap[c] == []: return True
            visitSet.add(c)
            for p in preMap[c]:
                if not dfs(p): return False
            visitSet.remove(c)
            preMap[c]= []
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True