class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mArea = 0
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            nonlocal mArea
            cArea = 1
            q = deque()
            q.append((r,c))
            grid[r][c]=0
            while q:
                row, col = q.pop()
                for dr,dc in directions:
                    nr, nc = row+dr, col+dc
                    if(nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==0):
                        continue
                    grid[nr][nc]=0
                    q.append((nr,nc))
                    cArea+=1
            mArea = max(mArea, cArea)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    bfs(r, c)
        return mArea     
            