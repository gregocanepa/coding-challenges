from typing import List
from collections import deque


def solution(S: str, grid: List[str]) -> int:
    # ... (the code snippet you provided remains the same)

    # Calculate the minimum moves required using BFS
    def bfs(start_pos, remaining_letters):
        visited = set()
        queue = deque([(start_pos, remaining_letters, 0)])

        while queue:
            (row, cell), letters, moves = queue.popleft()

            if not letters:
                return moves

            if (row, cell) in visited:
                continue

            visited.add((row, cell))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_cell = row + dr, cell + dc

                if 0 <= new_row < len(grid) and 0 <= new_cell < len(grid[0]):
                    new_cell_contents = grid[new_row][new_cell]

                    if new_cell_contents in letters:
                        new_letters = letters - set(new_cell_contents)
                        queue.append(((new_row, new_cell), new_letters, moves + 1))

        return -1

    target_letters = set(S)
    start_positions = [(pos["row"], pos["cell"]) for pos in dict_of_letters.values()]

    min_moves = float("inf")

    for start_pos in start_positions:
        moves = bfs(start_pos, target_letters)
        if moves != -1:
            min_moves = min(min_moves, moves)

    return min_moves if min_moves != float("inf") else -1


print(solution("XZZY", [".Z.", "XBB", "..A"]))
