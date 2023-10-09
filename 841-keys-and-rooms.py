import time
from collections import deque
from typing import List, Optional

class Solution:
    """Starting at node 0 for the given graph adjacency list, determine if every other node can be reached"""

    #   runtime: beats 99%
    def canVisitAllRooms_DFS(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def DFS(room: int):
            if room in visited:
                return
            visited.add(room)
            for next_room in rooms[room]:
                DFS(next_room)

        DFS(0)
        return len(visited) == len(rooms)


    #   runtime: beats 97%
    def canVisitAllRooms_BFS(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        queue.append(0)

        while len(queue) > 0:
            current = queue.popleft()
            visited.add(current)
            for next_room in rooms[current]:
                if next_room in visited:
                    continue
                queue.append(next_room)

        return len(visited) == len(rooms)


s = Solution()
test_functions = [ s.canVisitAllRooms_DFS, s.canVisitAllRooms_BFS, ]

inputs = [ [[1],[2],[3],[]], [[1,3],[3,0,1],[2],[0]], ]
checks = [ True, False, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for rooms, check in zip(inputs, checks):
        print(f"rooms=({rooms})")
        result = f(rooms)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

