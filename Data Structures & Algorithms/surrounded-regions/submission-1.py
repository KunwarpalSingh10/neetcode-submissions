class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Questions:
        Identify Problem: This is a graph problem that could be solved using bfs
        Approach: We look at every cell in the board and we check if it is equal to "O". If it is then we would have a bfs search on it, that checks the whole region where if any of them touch the edge we would replace with "X" otherwise we would keep looking at the whole and mark it as visited.
        Time Complexity: O(m * n), where m = number of rows and n = number of columns, iterate over the whole board once.
        Space Complexity: O(m * n), where m = number of rows and n = number of columns, we store the whole board in the set one time.
        Mistake: I forgot to expand the neighbors forward in bfs and also forgot the to put (r, c) for checking in set.
        """
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            surrounded = True
            switch = set()
            visited.add((r, c))
            switch.add((r, c))
            while q:
                qr, qc = q.popleft()
                directions = [[1,0], [-1,0], [0, -1], [0, 1]]
                if qr == 0 or qr == rows - 1 or qc == 0 or qc == cols - 1:
                    surrounded = False
                for dr, dc in directions:
                    hr, hc = qr + dr, qc + dc
                    if hr in range(rows) and hc in range(cols) and board[hr][hc] == "O" and (hr, hc) not in visited:
                        visited.add((hr, hc))
                        switch.add((hr, hc))
                        q.append((hr, hc))
                        if hr == 0 or hr == rows - 1 or hc == 0 or hc == cols - 1:
                            surrounded = False
            if surrounded:
                for sr, sc in switch:
                    board[sr][sc] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    bfs(r, c)

        