class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # This uses breath first search
        if not grid:
            return 0
        visit = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            
            while q:
                length = len(q)
                row, col = q.popleft()

                # we get this by looking at columns and rows
                distances = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in distances:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))

                    


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    visit.add((r,c))
                    islands += 1
                    bfs(r,c)
        
        return islands


