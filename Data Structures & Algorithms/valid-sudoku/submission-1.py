class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowvisited = defaultdict(set)
        columnvisited = defaultdict(set)
        gridvisited = defaultdict(set)
        length = 9
        for i in range(length):
            for j in range(length):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rowvisited[i] or board[i][j] in columnvisited[j] or board[i][j] in gridvisited[(i // 3, j // 3)]):
                    return False
                columnvisited[j].add(board[i][j])
                rowvisited[i].add(board[i][j])
                gridvisited[(i // 3, j // 3)].add(board[i][j])
        return True
