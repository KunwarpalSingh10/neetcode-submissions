class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Time Complexity: O(n * m)
        Space Complexity: O(n * m)
        """
        visited = set()
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        count = 1

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))


        while q:
            for _ in range(len(q)):
                qr, qc = q.popleft()
                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    hr, hc = dr + qr, dc + qc
                    if hr in range(rows) and hc in range(cols) and (hr, hc) not in visited and grid[hr][hc] == 2147483647:
                        grid[hr][hc] = count
                        visited.add((hr,hc))
                        q.append((hr, hc))
            count += 1