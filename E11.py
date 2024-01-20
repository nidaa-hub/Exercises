def reach_target(grid, start, target, k):
    def dfs(x, y, moves_left):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] == 1 or visited[x][y] or moves_left < 0:
            return False
        if x == target[0] and y == target[1]:
            return True
        visited[x][y] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            if dfs(x + dx, y + dy, moves_left - 1):
                return True
        visited[x][y] = False
        return False
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    return dfs(start[0], start[1], k)


n = 3
m = 3
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
start = (0, 0)
target = (2, 2)
k = 6

print(reach_target(grid, start, target, k))
