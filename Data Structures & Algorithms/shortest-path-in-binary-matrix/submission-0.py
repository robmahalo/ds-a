class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        visited = set([(0,0)])
        q = deque([(0,0)])
        length = 1

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
            
                directions = [[1,0], [-1,0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == 1):
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1