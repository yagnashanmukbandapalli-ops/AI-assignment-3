import heapq
import random

GRID_SIZE = 70

def create_grid(density):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    obstacle_count = int(GRID_SIZE * GRID_SIZE * density)

    for _ in range(obstacle_count):
        x = random.randint(0, GRID_SIZE-1)
        y = random.randint(0, GRID_SIZE-1)
        grid[x][y] = 1

    return grid


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    nodes_explored = 0

    while open_set:

        _, current = heapq.heappop(open_set)
        nodes_explored += 1

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, nodes_explored

        x, y = current

        neighbors = [
            (x+1,y),(x-1,y),(x,y+1),(x,y-1)
        ]

        for nx, ny in neighbors:

            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:

                if grid[nx][ny] == 1:
                    continue

                tentative = g_score[current] + 1

                if (nx,ny) not in g_score or tentative < g_score[(nx,ny)]:
                    g_score[(nx,ny)] = tentative
                    f = tentative + heuristic((nx,ny), goal)

                    heapq.heappush(open_set, (f,(nx,ny)))
                    came_from[(nx,ny)] = current

    return None, nodes_explored


density_levels = {
    "low":0.1,
    "medium":0.2,
    "high":0.3
}

density_choice = input("Choose density (low/medium/high): ")

grid = create_grid(density_levels[density_choice])

start = (0,0)
goal = (69,69)

path, explored = astar(grid, start, goal)

if path:
    print("Path Found")
    print("Path Length:", len(path))
else:
    print("No Path Found")

print("Nodes Explored:", explored)
