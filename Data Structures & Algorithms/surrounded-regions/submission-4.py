class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows, cols = len(board), len(board[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            edge = False
            change = set()
            change.add((r,c))
            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                qr,qc = q.popleft()
                if qr == 0 or qr == rows - 1 or qc == 0 or qc == cols - 1:
                    edge = True
                for dr, dc in directions:
                    hr, hc = qr + dr, qc + dc
                    if hr in range(rows) and hc in range(cols) and board[hr][hc] == "O" and (hr, hc) not in visited:
                        visited.add((hr, hc))
                        change.add((hr,hc))
                        q.append((hr, hc))
            if not edge:
                for er, ec in change:
                    board[er][ec] = "X"


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and board[r][c] == "O":
                    bfs(r, c)
