class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time Complexity: O(m * n), where m = len(grid) and n = len(grid[0])
        Space Complexity: O(m * n), worst case we store every cell in the grid in set
        """
        visited = set()
        res = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))

            while q:
                node = q.popleft()
                directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
                for dr, dc in directions:
                    hr, hc = dr + r, dc + c
                    if hr in range(rows) and hc in range(cols) and (hr,hc) not in visited and grid[hr][hc] == "1":
                        visited.add((hr,hc))
                        bfs(hr, hc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res
