def dynamic_navigation(grid, start, goal):

    current = start

    while current != goal:

        path, _ = astar(grid, current, goal)

        if not path:
            print("No safe path available")
            return

        for step in path[1:]:

            # simulate dynamic obstacle appearing
            if random.random() < 0.05:
                x,y = step
                grid[x][y] = 1
                print("Obstacle detected, replanning...")
                break

            current = step

            if current == goal:
                print("Goal reached!")
                return
