class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time Complexity: O(V + E), number of courses + number of prerequisites
        Space Complexity: O(V + E), number of courses + number of prerequisites
        """
        hashmap = defaultdict(list)
        visiting = set()
        for curr, prereq in prerequisites:
            hashmap[curr].append(prereq)
        
        def dfs(course):
            if course in visiting:
                return False
            if hashmap[course] == []:
                return True
            
            visiting.add(course)
            for p in hashmap[course]:
                if not dfs(p):
                    return False
            visiting.remove(course)
            hashmap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True