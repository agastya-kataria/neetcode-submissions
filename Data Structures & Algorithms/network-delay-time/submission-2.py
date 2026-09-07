class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        visit = set()
        adj = [[] for _ in range(n+1)]
        for u, v, t in times:
            adj[u].append((v,t))
        
        minHeap = [(0,k)]
        
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in visit: continue
            visit.add(v1)
            res = w1

            for v2, w2 in adj[v1]:
                heapq.heappush(minHeap, (w1+w2,v2))
        
        return res if len(visit) == n else -1
            

        