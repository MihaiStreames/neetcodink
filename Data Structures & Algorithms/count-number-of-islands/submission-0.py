class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        def dfs(r: int, c: int):
            if r < 0 or r >= len(grid):
                return
            if c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return
            if (r, c) in visited:
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)

        return res