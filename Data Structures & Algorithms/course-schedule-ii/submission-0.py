class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Identify Problem: Graph where we build off of order.
        Approach: We will build a hashmap that maps the course numbers(0 - (numCourses - 1)) to the prerequisites that associated with that courses. Then we will use dfs and find if the list is valid and if it is then we append it to the right of the result list.
        Time Complexity: O(V + E), V is the number of courses and E is the number of prequisites
        Space Complexity: O(V + E),  V is the number of courses and E is the number of prequisites
        Mistake: We will need to have another set because courses that were empty or had no prerequisites never got appended
        """
        hashmap = defaultdict(list)
        visited = set()
        visiting = set()
        res = []
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        # Here we will have 2 sets, once visited set that stores nodes that have been added to res and there will be a visiting set that stores nodes that will be used to check if there is cycle.
        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
                
            visiting.add(c)

            for pre in hashmap[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
