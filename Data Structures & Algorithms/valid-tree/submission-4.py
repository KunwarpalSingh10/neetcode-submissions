class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Identify Problem: Graph DFS search to see how many edges
        Approach: We have to use the rule that there are n - 1 edges and n vertices in a tree compared to a graph that does not have any rule to it. So we have to find the number of edges within the graph. We can do this with dfs. One way this can be done is using the length of edges and comparing it to n where n == len(edges) + 1
        Time Complexity: O(V + E), We look both at number of vertices and edges
        Space Complexity: O(V + E), We look both at number of vertices and edges
        Mistak1: A tree cannot have a cycle even if it is undirected but a undirected graph can have cyles.
        Mistake2: Since it is undirected it would going two directions and so we would collect edges going both directions in hashmap.
        Mistake3: We dont need to check for cycles if we are already checking for the V <-> E - 1
        """
        if n != len(edges) + 1:
            return False

        hashmap = defaultdict(list)
        visited = set()

        for curr, nei in edges:
            hashmap[curr].append(nei)
            hashmap[nei].append(curr)

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nei in hashmap[node]:
                dfs(nei)
        dfs(0)
        return n == len(visited)




