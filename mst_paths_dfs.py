import numpy as np

def path_weights_dfs(mst_adj_matr):
    n_nodes = len(mst_adj_matr)
    paths = np.zeros((n_nodes, n_nodes))

    # Step 1: find starting node
    for node in range(n_nodes):
        nonzero_count = np.count_nonzero(mst_adj_matr[node])
        if nonzero_count == 1:
            source_node = node
            break
            
    # initialize containers
    node_visited = np.full(n_nodes, False, dtype=bool)
    fork_node_path = []
    visited_leaves = []
    pre_leaf_count = []
    path_weights = np.array([])
    current_node = source_node

    # Step 4: repeat until every node was visited
    while not all(node_visited):
        node_visited[current_node] = True

        # Step 2: find the next node, that has not yet been visited
        next_nodes = np.nonzero(mst_adj_matr[current_node])[0]
        for nn in next_nodes:
            if not node_visited[nn]:
                next_node = nn
                break

        # Step 3: carried out if the visited node is a leaf
        if len(next_nodes) == 1:
            visited_leaves.append(current_node)
            path_weights = np.append(path_weights, 0)

        # jump back to the last visited fork
        if current_node == next_node:
            next_node = fork_node_path.pop()
            pre_leaf_ind = pre_leaf_count.pop()

            # backtrack the path weights
            backtrack_path_weight = path_weights[0]-paths[visited_leaves[0]][next_node]
            path_weights[:pre_leaf_ind] -= backtrack_path_weight
            path_weights[pre_leaf_ind:] += backtrack_path_weight
            current_node = next_node
            continue

        # Step 3: carried out if the visited node is a fork
        if len(next_nodes) >= 3:
            fork_node_path.append(current_node)
            pre_leaf_count.append(len(visited_leaves))

        # Step 2: update the traveled distance
        path_weights += mst_adj_matr[current_node][next_node]
        paths[visited_leaves, next_node] = path_weights

        # Step 2: travel to the next node
        current_node = next_node
    
    return paths
