class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(m * n), m = len(grid), n = len(grid[0])
        Space Complexity: O(m * n), m = len(grid), n = len(grid[0])
        """
        visited = set()
        maxarea = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                up = 1 + dfs(r + 1, c)
                down = 1 + dfs(r - 1, c)
                right = 1 + dfs(r, c + 1)
                left = 1 + dfs(r, c - 1)
                return up + down + right + left
            else:
                return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxarea = max(dfs(r, c), maxarea)
        return maxarea // 4
                    