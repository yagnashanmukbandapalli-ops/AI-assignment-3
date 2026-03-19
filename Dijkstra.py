import heapq

# Graph of Indian cities with distances (km)
graph = {
    "Delhi": {"Jaipur": 280, "Lucknow": 500, "Chandigarh": 250},
    "Jaipur": {"Delhi": 280, "Ahmedabad": 660},
    "Lucknow": {"Delhi": 500, "Patna": 530},
    "Chandigarh": {"Delhi": 250, "Shimla": 115},
    "Ahmedabad": {"Jaipur": 660, "Mumbai": 530},
    "Patna": {"Lucknow": 530, "Kolkata": 620},
    "Shimla": {"Chandigarh": 115},
    "Mumbai": {"Ahmedabad": 530},
    "Kolkata": {"Patna": 620}
}

def dijkstra(graph, start):
    priority_queue = [(0, start)]
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous = {}

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


def get_path(previous, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = previous.get(current)
        if current is None:
            return None
    path.append(start)
    path.reverse()
    return path


start = input("Enter start city: ")
goal = input("Enter destination city: ")

distances, previous = dijkstra(graph, start)
path = get_path(previous, start, goal)

print("Shortest Distance:", distances[goal], "km")
print("Path:", " -> ".join(path))
