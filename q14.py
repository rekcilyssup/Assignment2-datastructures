"""Module for counting islands in a grid."""


def count_islands(input_matrix):
    """
    Function to count the number of islands in a 2D matrix.
    An island is a group of connected 1's (horizontally, vertically,
    and diagonally).
    Example:
    Input: [[1,1,0,0],
            [0,1,0,1],
            [1,0,0,1]]
    Output: 2 (with diagonals, the top-left group becomes one island)
    """
    if not input_matrix or len(input_matrix) == 0:
        return 0

    rows = len(input_matrix)
    cols = len(input_matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    island_count = 0

    def dfs(row, col):
        """Mark all connected 1's as visited using DFS."""
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if visited[row][col] or input_matrix[row][col] == 0:
            return

        visited[row][col] = True

        # we explore all 8 direction
        dfs(row - 1, col)      # Up
        dfs(row + 1, col)      # Down
        dfs(row, col - 1)      # Left
        dfs(row, col + 1)      # Right
        dfs(row - 1, col - 1)  # Top-left diagonal
        dfs(row - 1, col + 1)  # Top-right diagonal
        dfs(row + 1, col - 1)  # Bottom-left diagonal
        dfs(row + 1, col + 1)  # Bottom-right diagonal

    for row in range(rows):
        for col in range(cols):
            if input_matrix[row][col] == 1 and not visited[row][col]:
                dfs(row, col)
                island_count += 1

    return island_count


if __name__ == "__main__":
    count_islands([[1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 0, 1]])
