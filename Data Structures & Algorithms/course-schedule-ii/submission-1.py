class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        visited = set()
        visiting = set()
        res = []
        hp = defaultdict(list)
        for curr, prev in prerequisites:
            hp[curr].append(prev)

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for p in hp[course]:
                if not dfs(p):
                    return False
            visited.add(course)
            visiting.remove(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
