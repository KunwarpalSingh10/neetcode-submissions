class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Identify Problem: Graph, where we check if courses can be completed
        Approach: We would create a hashmap that stores a list of prerequisites relative to each course number and then we will use dfs on each course to find if each of them can be completed.
        Time Complexity: O(V + E), where V is the number of courses, and E is the number of prerequisites
        Space Complexity: O(V + E), where V is the number of courses, and E is the number of prerequisites
        """
        hashmap = defaultdict(list)
        visit = set()
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        def dfs(c):
            if c in visit:
                return False
            if hashmap[c] == []:
                return True
            visit.add(c)
            
            for cs in hashmap[c]:
                if not dfs(cs):
                    return False

            visit.remove(c)
            hashmap[c] = []
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

