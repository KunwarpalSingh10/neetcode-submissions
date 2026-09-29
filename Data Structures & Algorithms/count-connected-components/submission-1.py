class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        hashmap = defaultdict(list)
        res = 0
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
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
    
