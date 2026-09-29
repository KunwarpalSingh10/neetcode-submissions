class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        q = collections.deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh != 0:
            for _ in range(len(q)):
                qr, qc = q.popleft()
                directions = [[1,0], [-1,0], [0,-1],[0,1]]
                for dr, dc in directions:
                    hr, hc = qr + dr, dc + qc
                    if hr in range(rows) and hc in range(cols) and (hr,hc) not in visited and grid[hr][hc] == 1:
                        grid[hr][hc] = 2
                        visited.add((hr, hc))
                        q.append((hr, hc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        