class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        q = deque()

        def rot(r, c):
            nonlocal fresh
            if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]==0 or grid[r][c]==2): return
            grid[r][c] = 2
            fresh-=1
            q.append((r,c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        
        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r+1,c)
                rot(r-1,c)
                rot(r,c+1)
                rot(r,c-1)
            time+=1
        
        return time if fresh==0 else -1


            
        