class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    visit.add((r,c))
                    q.append((r,c))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] == -1 or (nr,nc) in visit:
                        continue
                    
                    grid[nr][nc] = dist+1
                    q.append((nr,nc))
                    visit.add((nr,nc))
            dist+=1
        
        