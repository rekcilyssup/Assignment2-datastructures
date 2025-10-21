"""Module for graph connectivity operations."""


def is_strongly_connected_graph(matrix):
    """
    Check if the given directed graph is strongly connected or not.
    A directed graph is strongly connected if there is a path from
    every node to every other node.

    Example:
    Input: [[0,1,0],[0,0,1],[1,0,0]]
    (0→1, 1→2, 2→0 - a cycle)
    Output: True

    Example:
    Input: [[0,1,0],[0,0,1],[0,0,0]]
    (0→1→2, but no path back)
    Output: False
    """
    if not matrix or len(matrix) == 0:
        return True

    num_nodes = len(matrix)

    def can_reach_all(start):
        """Check if we can reach all nodes from start node using DFS."""
        visited = [False] * num_nodes
        stack = [start]

        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True

            # Add all neighbors to stack
            for neighbor in range(num_nodes):
                if matrix[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

        # Check if all nodes were visited
        return all(visited)

    # Check if every node can reach all other nodes
    return all(can_reach_all(node) for node in range(num_nodes))


if __name__ == "__main__":
    is_strongly_connected_graph([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
