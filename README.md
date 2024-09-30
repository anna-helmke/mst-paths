# Calculate MST paths fast using DFS
An algorithm that calculates all paths in a minimum spanning tree (MST).

I designed this algorithm as part of my bachelor thesis, when I had to find the longest path of a multitude of MSTs as a representaion of the length of different star clusters.  
Its based on depth first search and runs in $O(n)$, making it quick even for large clusters. However the space complexity is $O(n^2)$ as it uses a $n \times n$-Matrix to store all path lengths.

## How it works
### 3 different node types:
`leaf`: exactly one edge  
`fork`: more than two edges  
`normal`: exactly two edges  

### 5 containers:
`visited_leaves`: list; stores all already visited `leaves`  
`fork_node_path`: list: stores all `forks` that are on the current path  
`pre_leaf_count`: list; counts the number of visited leaves before encountering a certain `fork`  
`path_weights`: list; stores all currently updating path weights from all visited `leaves` to the encountered nodes  
`paths`: nxn-Matrix; stores the weight for all paths (result)

### Here is a quick overview of its process:
Step 1: choose random `leaf` as source node  
Step 2: mark node as visited -> travel to next not yet visited node -> update `path_weights` and `paths`  
Step 3: repeat Step 2 until `fork` or `leaf`  
<ul> `fork`: update `fork_node_path` and `pre_leaf_count` </ul>  
<ul> `leaf`: update `visited_leaves` -> jump back to last `fork` -> update `path_weights` </ul>  
Step 4: repeat Step 3 until all nodes have been visited  
return: `paths`
