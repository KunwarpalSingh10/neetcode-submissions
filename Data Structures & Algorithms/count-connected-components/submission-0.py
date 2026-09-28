class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Identify Problem: Undirected Graph Problem
        Approach: We do this by adding both sides of the edges to a adjectcy list and then using dfs on every to check which group of nodes are connected together.
        Time Complexity: O(V + E) where V is number of vertices and E is number of edges
        Space Complexity: O(V + E) where V is number of vertices and E is number of edges
        """
        hashmap = defaultdict(list)
        visited = set()
        for curr, nei in edges:
            hashmap[curr].append(nei)
            hashmap[nei].append(curr)

        def dfs(node):
            visited.add(node)
            for nei in hashmap[node]:
                if nei not in visited:
                    dfs(nei)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count





        