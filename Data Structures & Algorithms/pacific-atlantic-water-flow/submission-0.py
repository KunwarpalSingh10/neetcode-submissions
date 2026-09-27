class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Identify Problem: We use BFS in order to see which cells are touch both pacific and altanic ocean.
        Approach: Look at which cells are touch the each side by doing search starting from each side and not from a individual cell because then it would be O(m * n)^2 complexity. After this we look at every cell in the grid and see which ones are both pacific and altantic.
        Time Complexity: O(m * n), as we are iterating over the whole grid once in one loop. m = len(columns), n = len(rows)
        Space Complexity: O(m * n), worst case we are storing all of the grid in either set
        """
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def bfs(r, c, s):
            q = collections.deque()
            q.append((r,c))
            s.add((r,c))

            while q:
                qr, qc = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    hr, hc = dr + qr, dc + qc
                    if hr in range(rows) and hc in range(cols) and (hr, hc) not in s and heights[hr][hc] >= heights[qr][qc]:
                        s.add((hr, hc))
                        q.append((hr,hc))

                    

        for i in range(rows):
            bfs(i, 0, pacific)
            bfs(i,cols - 1, atlantic)

        for i in range(cols):
            bfs(0,i, pacific)
            bfs(rows - 1, i, atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in atlantic and (r,c) in pacific:
                    res.append([r,c])

        return res
        