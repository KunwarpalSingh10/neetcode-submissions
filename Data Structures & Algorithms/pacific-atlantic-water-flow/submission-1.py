class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])
        res = []

        def bfs(r, c, s):
            q = collections.deque()
            q.append((r, c))
            s.add((r,c))
            while q:
                qr, qc = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    hr, hc = dr + qr, dc + qc
                    if hr in range(rows) and hc in range(cols) and (hr,hc) not in s and heights[hr][hc] >= heights[qr][qc]:
                        s.add((hr,hc))
                        q.append((hr,hc))


        for r in range(rows):
            bfs(r, 0, pacific)
            bfs(r, cols - 1, atlantic)

        for c in range(cols):
            bfs(0, c, pacific)
            bfs(rows - 1, c, atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r, c])

        return res

