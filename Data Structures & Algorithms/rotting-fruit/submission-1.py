class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # 1. Multi-Source Initialization
        # Scan the entire grid once to queue all starting points and count targets
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Check Down
                if r + 1 < ROWS and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh_count -= 1
                    queue.append((r + 1, c))
                    
                # Check Up
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh_count -= 1
                    queue.append((r - 1, c))
                    
                # Check Right
                if c + 1 < COLS and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh_count -= 1
                    queue.append((r, c + 1))
                    
                # Check Left
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh_count -= 1
                    queue.append((r, c - 1))
                    
            minutes += 1
        return minutes if fresh_count == 0 else -1