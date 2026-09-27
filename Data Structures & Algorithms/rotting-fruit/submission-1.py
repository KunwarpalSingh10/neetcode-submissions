class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Identify Problem: BFS to count layer by layer counts as a minute passing by
        Approach: Go through the matrix using two for loops and search for rooten fruits and add those to the queue. After this we run BFS after collecting looking at the whole matrix for rooten fruits. We will also be looking at the number of fresh fruits while we go through the array like this. We will use BFS by updating the number of fresh fruits and putting them into the queue.
        Time Complexity: O(m * n), where m is the number of columns in grid and n is number of rows in grid
        Space Complexity: O(m * n), as we may need to store every point in grid if need when the grid is completely full and not empty
        Mistake: We don't need set because we can just change the grid in place.
        Lesson Learned: We use the for _ in range() to make it easy to identify each level update time
        """

        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = [[-1,0], [1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    hr, hc = dr + r, dc + c
                    if hr in range(rows) and hc in range(cols) and grid[hr][hc] == 1:
                        grid[hr][hc] = 2
                        fresh -= 1
                        q.append((hr,hc))
            time += 1
        if fresh == 0:
            return time
        return -1
        


