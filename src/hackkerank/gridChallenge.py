def gridChallenge(grid):
    n = len(grid)
    m = len(grid[0])
    
    for i in range(n):
        grid[i] = ''.join(sorted(grid[i]))

    for j in range(m):
        for i in range(n-1):
            if grid[i][j] > grid[i+1][j]:
                return "NO"

    return "YES"