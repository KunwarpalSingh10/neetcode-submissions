class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maximum = 0
        area = 0
        visit = set()

        def bfs(r, c, area):
            q = collections.deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0,-1], [0,1]]
                for dr, dc in directions:
                    r, c = row + dr, dc + col
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visit:
                        visit.add((r, c))
                        q.append((r,c))
                        area += 1
            return area
                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    visit.add((r,c))
                    maximum = max(maximum, bfs(r, c, 1))
        return maximum
