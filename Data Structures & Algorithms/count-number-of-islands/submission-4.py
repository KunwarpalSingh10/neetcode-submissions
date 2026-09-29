class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time Complexity: O(m * n), where m = len(grid) and n = len(grid[0])
        Space Complexity: O(m * n), worst case we store every cell in the grid in set
        """
        visited = set()
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == "1":
                visited.add((r,c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)
            

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res
