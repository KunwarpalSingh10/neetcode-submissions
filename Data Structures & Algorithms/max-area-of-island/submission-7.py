class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(m * n), m = len(grid), n = len(grid[0])
        Space Complexity: O(m * n), m = len(grid), n = len(grid[0])
        """
        visited = set()
        maxarea = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            total = 1
            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                rq, cq = q.popleft()
                for dr, dc in directions:
                    hr, hc = dr + rq, dc + cq
                    if hr in range(rows) and hc in range(cols) and grid[hr][hc] == 1 and (hr,hc) not in visited:
                        visited.add((hr, hc))
                        q.append((hr, hc))
                        total += 1
            return total
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxarea = max(bfs(r,c), maxarea)

        return maxarea
                    