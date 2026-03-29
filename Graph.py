def print_graph(graph):
    for vertex in graph:
        print(f'{vertex} 》{graph[vertex]}')


def graph_insert(graph, vertex):
    if vertex not in graph:
        graph[vertex] = []
    else:
        print(f'vertex {vertex} already exists')


def graph_delete(graph, vertex):
    if vertex in graph:
        for neighbors in graph[vertex]:
            if vertex in graph[neighbors]:
                graph[neighbors].remove(vertex)
        del graph[vertex]


def graph_insert_edge(graph, vertex1, vertex2):
    if vertex1 in graph and vertex2 in graph:
        if vertex1 not in graph[vertex2]:
            graph[vertex2].append(vertex1)
        if vertex2 not in graph[vertex1]:
            graph[vertex1].append(vertex2)


def graph_delete_edge(graph, vertex1, vertex2):
    if vertex1 in graph and vertex2 in graph:
        if vertex1 in graph[vertex2]:
            graph[vertex2].remove(vertex1)
        if vertex2 in graph[vertex1]:
            graph[vertex1].remove(vertex2)


def graph_is_path(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    if start == target:
        return True
    visited.add(start)
    for neighbors in graph[start]:
        if neighbors == target:
            return True
        if neighbors not in visited:
            if graph_is_path(graph, neighbors, target, visited):
                return True
    return False


def graph_shortest_path(graph, start, target):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        current = path[-1]
        if current == target:
            return path
        else:
            for neighbor in graph[current]:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    queue.append(new_path)
    return None


def weighted_graph_shortest_distance(graph, start):
    distances = {node: 0 if node == start else float('inf') for node in graph}
    visited = set()
    while len(visited) < len(distances):
        current, min_distance = None, float('inf')
        for node in distances:
            if node not in visited and distances[node] < min_distance:
                current, min_distance = node, distances[node]
        if current is None:
            break
        visited.add(current)
        for neighbor, weight in graph[current]:
            new_dist = min(distances[current] + weight, distances[neighbor])
            distances[neighbor] = new_dist
    return distances


def graph_mst(graph, start):
    mst, visited = [], {start}
    edges = [(weight, start, to) for to, weight in graph[start]]
    while len(visited) < len(graph):
        weight, frm, to = edges[0]
        for curr_weight, curr_frm, curr_to in edges:
            if curr_weight < weight:
                weight, frm, to = curr_weight, curr_frm, curr_to
        edges.remove((weight, frm, to))
        if to not in visited:
            visited.add(to)
            mst.append((f'{frm} 》({weight}) 》{to}'))
        for next_to, next_weight in graph[to]:
            if next_to not in visited:
                edges.append((next_weight, to, next_to))
    return mst


def graph_topological_sort(graph):
    graph_copy = {node: neighbors[:] for node, neighbors in graph.items()}
    result = []
    while graph_copy:
        queue = [node for node in graph_copy if all(node not in neighbors for neighbors in graph_copy.values())]
        if not queue:
            print("Error - the graph includes cycle")
            return
        for node in queue:
            result.append(node)
            del graph_copy[node]
    return result


def graph_all_edges_path(graph, start):
    copy_graph = {node: graph[node][:] for node in graph}
    path = []

    def visit(node):
        while copy_graph[node]:
            current = copy_graph[node].pop()
            copy_graph[current].remove(node)
            visit(current)
        path.append(node)

    visit(start)
    return path[::-1]


def weighted_graph_shortest_distances(graph):
    nodes = list(graph.keys())
    dist = {node: {neighbor: float('inf') for neighbor in nodes} for node in nodes}
    for node in nodes:
        dist[node][node] = 0
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight
    for node in nodes:
        for neighbor in nodes:
            for via in nodes:
                dist[node][neighbor] = min(dist[node][neighbor], dist[node][via] + dist[via][neighbor])
    return dist


def graph_find_bridges(graph):
    bridges, checked = [], set()
    for node in graph:
        for neighbor in graph[node]:
            edge = tuple(sorted([node, neighbor]))
            if edge not in checked:
                graph_delete_edge(graph, node, neighbor)
                if not graph_is_path(graph, node, neighbor):
                    bridges.append(edge)
                graph_insert_edge(graph, node, neighbor)
                checked.add(edge)
    return bridges


def weighted_graph_shortest_distances_with_negatives(graph, start):
    distances = {node: 0 if node == start else float('inf') for node in graph}
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                distances[neighbor] = min(distances[neighbor], distances[node] + weight)
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = float('-inf')
    return distances


def weighted_graph_shortest_all_distances_with_negatives(graph):
    graph['temp'] = []
    for node in graph:
        if node != 'temp':
            graph['temp'].append((node, 0))
    pots, new_graph = weighted_graph_shortest_distances_with_negatives(graph, 'temp'), {}
    for node in graph:
        if node == 'temp':
            continue
        new_graph[node] = []
        for neighbor, weight in graph[node]:
            new_graph[node].append((neighbor, (weight + pots[node] - pots[neighbor])))
    del graph['temp']
    result = {}
    for node in new_graph:
        dists = weighted_graph_shortest_distance(new_graph, node)
        right_dists = {neighbor: dists[neighbor] + pots[neighbor] - pots[node] for neighbor in dists}
        result[node] = right_dists
    return result


def graph_find_SCCs(graph):
    visited = set()
    finished = []

    def DFS1(start):
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                DFS1(neighbor)
        finished.append(start)

    reversed_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    for node in graph:
        if node not in visited:
            DFS1(node)
    visited.clear()
    SCCs = []

    def DFS2(start, comp):
        visited.add(start)
        comp.append(start)
        for neighbor in reversed_graph[start]:
            if neighbor not in visited:
                DFS2(neighbor, comp)

    for node in reversed(finished):
        if node not in visited:
            comp = []
            DFS2(node, comp)
            SCCs.append(comp)
    return SCCs


def graph_is_Eulerian(graph):
    is_path = is_circuit = True
    start_nodes, finish_nodes = [], []
    for node in graph:
        in_degree = 0
        for other_node in graph:
            if node in graph[other_node]:
                in_degree += 1
        out_degree = len(graph[node])
        if in_degree != out_degree:
            is_circuit = False
        if out_degree == in_degree + 1:
            start_nodes.append(node)
        if in_degree == out_degree + 1:
            finish_nodes.append(node)
        if node not in start_nodes and node not in finish_nodes and in_degree != out_degree:
            is_path = False
        for neighbor in graph[node]:
            if not graph_is_path(graph, node, neighbor):
                print("No Eulerian path/circuit exists in the graph")
                return
    if len(start_nodes) != 1 or len(finish_nodes) != 1:
        is_path = False
    if is_path:
        return "Eulerian path exists in the graph"
    elif is_circuit:
        return "Eulerian circuit exists in the graph"


def weighted_graph_longest_path(graph):
    dag = graph_topological_sort(graph)
    distances = {node: 0 for node in graph}
    previous = {node: None for node in graph}
    for node in dag:
        for neighbor, weight in graph[node]:
            if distances[node] + weight > distances[neighbor]:
                distances[neighbor] = distances[node] + weight
                previous[neighbor] = node
    max_path_end = max(distances, key=lambda x: distances[x])
    max_path = []
    max_path_length = distances[max_path_end]
    while max_path_end:
        max_path.append(max_path_end)
        max_path_end = previous[max_path_end]
    max_path.reverse()
    return f"path is {max_path} and path's length is {max_path_length}"


def weighted_graph_shortest_path(graph):
    dag = graph_topological_sort(graph)
    distances = {node: 0 for node in graph}
    previous = {node: None for node in graph}
    for node in dag:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = distances[node] + weight
                previous[neighbor] = node
    min_path_end = min(distances, key=lambda x: distances[x])
    min_path = []
    min_path_length = distances[min_path_end]
    while min_path_end:
        min_path.append(min_path_end)
        min_path_end = previous[min_path_end]
    min_path.reverse()
    return f"path is {min_path} and path's length is {min_path_length}"


def graph_max_flow(graph, start, target):
    max_flow = 0
    def bfs(start, target):
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            current = path[-1]
            if current == target:
                return path
            else:
                for neighbor, cap in caps[current].items():
                    if neighbor not in path and cap > 0:
                        new_path = path + [neighbor]
                        queue.append(new_path)
        return None
    caps = {node: {neighbor: cap for neighbor, cap in graph[node]} for node in graph}
    while True:
        min_path = bfs(start, target)
        if min_path is None:
            break
        min_path_caps = []
        for i in range(len(min_path) - 1):
            node, neighbor = min_path[i], min_path[i + 1]
            cap = caps[node][neighbor]
            min_path_caps.append(cap)
        bottleneck = min(min_path_caps)
        max_flow += bottleneck
        for i in range(len(min_path) - 1):
            node, neighbor = min_path[i], min_path[i + 1]
            caps[node][neighbor] -= bottleneck
    return max_flow


def graph_coloring(graph, colors):
    colored = {node: None for node in graph}
    nodes = list(graph)
    def coloring(index):
        def is_legal(node, color):
            for neighbor in graph[node]:
                if color == colored[neighbor]:
                    return False
            return True
        if index == len(graph):
            return True
        node = nodes[index]
        for color in colors:
            if is_legal(node, color):
                colored[node] = color
                if coloring(index + 1):
                    return True
                else:
                    colored[node] = None
        return False
    if coloring(0):
        return colored
    else:
        return False


def graph_hemiltonian_cycles(graph):
    start = next(iter(graph))
    visited, path = {start}, [start]
    cycles = []
    def backtrack(current):
        if len(path) == len(graph):
            if start in graph[current]:
                cycles.append(path + [start])
            return
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                backtrack(neighbor)
                visited.remove(neighbor)
                path.pop()
    backtrack(start)
    if cycles:
        return cycles
    else:
        return "No Hemiltonian cycle found in the graph"


def graph_strong_k_length_cliques(graph, k):
    strong_cliques = []
    nodes = list(graph)
    def backtrack(start_index, current_clique):
        if len(current_clique) == k:
            strong_cliques.append(current_clique[:])
            return
        for i in range(start_index, len(nodes)):
            current = nodes[i]
            if all(current in graph[node] and node in graph[current] for node in current_clique):
                current_clique.append(current)
                backtrack(i + 1, current_clique)
                current_clique.pop()
    backtrack(0, [])
    return strong_cliques


def graph_min_FVS(graph):
    min_fvs, nodes = None, list(graph.keys())
    def graph_cycle(graph):
        path, visited = [], set()
        def dfs(node):
            path.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in path:
                    return path[path.index(neighbor):]
                if neighbor not in visited:
                    cycle = dfs(neighbor)
                    if cycle:
                        return cycle
            path.pop()
        for node in graph:
            cycle = dfs(node)
            if cycle:
                return cycle
        return None
    def backtrack(i, removed):
        nonlocal min_fvs
        if not graph_cycle({node: [neighbor for neighbor in graph[node] if neighbor not in removed] for node in graph if
                            node not in removed}):
            if not min_fvs or len(removed) < len(min_fvs):
                min_fvs = set(removed)
            return
        if i == len(nodes):
            return
        backtrack(i + 1, removed)
        removed.add(nodes[i])
        backtrack(i + 1, removed)
        removed.remove(nodes[i])

    backtrack(0, set())
    return min_fvs


def graph_max_IS(graph):
    best_set = []
    def is_legal(node, current_set):
        for other_node in current_set:
            if node in graph[other_node] or other_node in graph[node]:
                return False
        return True
    def backtrack(current_set, nodes_left):
        nonlocal best_set
        if len(current_set) + len(nodes_left) < len(best_set):
            return
        if not nodes_left:
            if len(current_set) > len(best_set):
                best_set = current_set[:]
            return
        node = nodes_left[0]
        rest = nodes_left[1:]
        backtrack(current_set, rest)
        if is_legal(node, current_set):
            current_set.append(node)
            backtrack(current_set, rest)
            current_set.pop()
    all_nodes = list(graph.keys())
    backtrack([], all_nodes)
    return best_set


def graph_min_DS(graph):
    best_set, nodes = None, list(graph.keys())
    def backtrack(i, current_set, covered):
        nonlocal best_set
        if all(node in covered for node in graph):
            if not best_set or len(current_set) < len(best_set):
                best_set = current_set[:]
            return
        if i == len(graph):
            return
        if best_set and len(current_set) >= len(best_set):
            return
        backtrack(i + 1, current_set, covered)
        added = set()
        if nodes[i] not in covered:
            covered.add(nodes[i])
            added.add(nodes[i])
            current_set.append(nodes[i])
            for neighbor in graph[nodes[i]]:
                if neighbor not in covered:
                    covered.add(neighbor)
                    added.add(neighbor)
            backtrack(i + 1, current_set, covered)
            current_set.pop()
            for node in added:
                covered.remove(node)
    backtrack(0, [], set())
    return best_set


def graph_max_clique(graph):
    best_clique = []
    def backtrack(current_clique, candidates):
        nonlocal best_clique
        if len(current_clique) > len(best_clique):
            best_clique = current_clique[:]
        if not candidates or len(current_clique) + len(candidates) <= len(best_clique):
            return
        for node in candidates:
            backtrack(current_clique + [node],
                      [neighbor for neighbor in candidates if neighbor in graph[node] and neighbor != node])
            backtrack(current_clique, [vertex for vertex in candidates if vertex != node])
    backtrack([], list(graph.keys()))
    return best_clique


def graph_max_IB(graph):
    best_set = []
    def is_bipartite(subgraph):
        colors = {}
        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if neighbor not in subgraph:
                    continue
                if neighbor not in colors:
                    if not dfs(neighbor, 1 - color):
                        return False
                elif colors[neighbor] == colors[node]:
                    return False
            return True
        for node in subgraph:
            if node not in colors:
                if not dfs(node, 0):
                    return False
        return True
    def backtrack(current_set, candidates):
        nonlocal best_set
        if len(current_set) + len(candidates) <= len(best_set):
            return
        if len(current_set) > len(best_set):
            best_set = current_set[:]
        for i, node in enumerate(candidates):
            if is_bipartite(current_set + [node]):
                backtrack(current_set + [node], candidates[i + 1:])
    backtrack([], list(graph))
    return best_set


graph1 = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
graph2 = {'A': [('B', 5), ('C', 2)], 'B': [('A', 5), ('C', 3)], 'C': [('A', 2), ('B', 3)]}
graph3 = {'A': ['B', 'C', 'D'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D'], 'D': ['A', 'B', 'C']}
graph4 = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
graph5 = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
graph6 = {'A': [('B', 8), ('C', 1)], 'B': [('A', 8), ('C', 6)], 'C': [('A', 1), ('B', 6)]}
graph7 = {'A': ['B', 'D'], 'B': ['A', 'C'], 'C': ['B'], 'D': ['A']}
graph8 = {'A': [('B', 12)], 'B': [('C', -3)], 'C': []}
graph9 = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['E'], 'D': ['E'], 'E': ['A', 'C']}
graph10 = {'A': ['B'], 'B': ['C'], 'C': ['D'], 'D': ['E'], 'E': []}
graph11 = {'A': [('B', 3)], 'B': [('C', 4)], 'C': [('D', 12)], 'D': [('E', 7)], 'E': []}
graph12 = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
graph13 = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': ['E', 'C'], 'E': ['A', 'C']}
graph14 = {'A': ['B', 'C', 'E'], 'B': ['C', 'A', 'D'], 'C': ['A', 'B', 'D'], 'D': ['B', 'C', 'E'], 'E': ['A', 'D']}
graph15 = {'A': ['B'], 'B': ['C'], 'C': [], 'D': ['B']}

graph_insert(graph1, 'D')
print('graph after insertion:')
print_graph(graph1)

graph_delete(graph1, 'C')
print('graph after deletion:')
print_graph(graph1)

graph_insert_edge(graph1, 'A', 'D')
print('graph after inserting an edge:')
print_graph(graph1)

graph_delete_edge(graph1, 'A', 'B')
print('graph after deleting an edge:')
print_graph(graph1)

if graph_is_path(graph1, 'B', 'D'):
    print("there is a path between the two vertices")
else:
    print("there is not a path between the two vertices")

shortest_path = graph_shortest_path(graph3, 'A', 'D')
print(f'the shortest path between the two vertices is {shortest_path}')

shortest_dist = weighted_graph_shortest_distance(graph2, 'A')
print(f'the shortest distances between the vertex to all the others is {shortest_dist}')

mst = graph_mst(graph2, 'A')
print(f'graph vertices connected by edges which maintains the minimal sum of weights: {mst}')

top_sorted_graph = graph_topological_sort(graph4)
print(f'topological sorted graph: {top_sorted_graph}')

all_edges_list = graph_all_edges_path(graph5, 'B')
print(f'all edges path in the graph: {all_edges_list}')

shortest_graph = weighted_graph_shortest_distances(graph6)
print(f'weighted graph with the shortest distances between all the vertices in the original graph: {shortest_graph}')

graph_bridges = graph_find_bridges(graph7)
print(f'all bridges in the graph: {graph_bridges}')

shortest_dist = weighted_graph_shortest_distances_with_negatives(graph8, 'B')
print(f'shortest distances between a vertice to all the others: {shortest_dist}')

shortest_dists = weighted_graph_shortest_all_distances_with_negatives(graph8)
print(f'shortest distances between all vertice to all the others: {shortest_dists}')

graph_SCCs = graph_find_SCCs(graph9)
print(f'all SCCs in the graph: {graph_SCCs}')

is_Eulerian = graph_is_Eulerian(graph10)
print(is_Eulerian)

shortest_path = weighted_graph_shortest_path(graph11)
print(f'shortest possible path in the graph: {shortest_path}')

longest_path = weighted_graph_longest_path(graph11)
print(f'longest possible path in the graph: {longest_path}')

max_flow = graph_max_flow(graph11, 'A', 'E')
print(f'maximal flow between the two vertices in the graph: {max_flow}')

colored = graph_coloring(graph12, ['red', 'blue', 'green'])
if not colored:
    print("the graph be colored with this amount of colors")
else:
    print(f'colored graph: {colored}')

hemiltonian_cycles = graph_hemiltonian_cycles(graph13)
print(f'all hemiltonian cycles in the graph: {hemiltonian_cycles}')

k = 3
print(f'all strong cliques in the graph of length {k}: {graph_strong_k_length_cliques(graph14, k)}')

min_fvs = graph_min_FVS(graph14)
print(f'min FVS in the graph: {min_fvs}')

max_is = graph_max_IS(graph15)
print(f'max IS in the graph: {max_is}')

min_ds = graph_min_DS(graph15)
print(f'min DS in the graph: {min_ds}')

max_clique = graph_max_clique(graph14)
print(f'max clique in the graph: {max_clique}')

max_IB = graph_max_IB(graph14)
print(f'max IB in the graph: {max_IB}')