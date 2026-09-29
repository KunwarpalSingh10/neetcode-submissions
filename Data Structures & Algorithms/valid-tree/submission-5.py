class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        nodes = 0
        # Check if number of edges is n - 1
        if len(edges) != n - 1:
            return False

        # To check if graph is connected to make tree, we have to check the node count by traversing
        hashmap = defaultdict(list)
        for curr, prev in edges:
            hashmap[curr].append(prev)
            hashmap[prev].append(curr)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in hashmap[node]:
                dfs(nei)
        
        dfs(0)

        return n == len(visited)

