import time
import copy

INF = 999

# Get user input for the graph
def get_user_input():
    graph = {}
    n = int(input("Enter number of routers: "))
    nodes = []

    print("Enter router names:")
    for _ in range(n):
        name = input().strip().upper()
        nodes.append(name)

    print("\nEnter cost between routers (999 for no direct link):")
    for i in range(n):
        graph[nodes[i]] = {}
        for j in range(n):
            cost = int(input(f"Cost from {nodes[i]} to {nodes[j]}: "))
            graph[nodes[i]][nodes[j]] = cost
    return graph

# Function to print routing tables
def print_tables(vectors):
    print("Routing Tables:")
    for node, table in vectors.items():
        print(f"{node}: {table}")
    print("-" * 50)

# Distance Vector Algorithm simulation
def distance_vector_routing(graph):
    vectors = {router: graph[router].copy() for router in graph}
    iteration = 0
    while True:
        changed = False
        print(f"Iteration {iteration}")
        print_tables(vectors)

        new_vectors = copy.deepcopy(vectors)
        
        for src in graph:
            for dest in graph:
                if src == dest:
                    continue
                min_cost = vectors[src][dest]
                for neighbor in graph[src]:
                    if neighbor != src and graph[src][neighbor] != INF:
                        new_cost = graph[src][neighbor] + vectors[neighbor][dest]
                        if new_cost < min_cost:
                            min_cost = new_cost
                            changed = True
                new_vectors[src][dest] = min_cost

        vectors = new_vectors
        iteration += 1
        time.sleep(1)
        if not changed:
            print(f"Converged after {iteration} iterations.\n")
            break

    print("Final Routing Tables:")
    print_tables(vectors)

# Main
graph = get_user_input()
distance_vector_routing(graph)
