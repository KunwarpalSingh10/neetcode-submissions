class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Identify Problem: Graph, we search the graph with bfs\
        Approach: We map each course to its prerequisites and then we run a dfs that goes through each of the prerequites until a course without prerequites is found. We also have a visit set that tracks if the same prequite is seen again and if it is then we return False otherwise we return true
        Time Complexity: O(m + p) where m is number of courses and p is number of prequisites
        Space Complexity: O(m) where m is the number of courses
        """
        h = defaultdict(list)

        for crs, pre in prerequisites:
            h[crs].append(pre)

        visit = set()

        def dfs(c):
            if c in visit:
                return False
            if h[c] == []:
                return True
            visit.add(c)

            for pre in h[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)
            h[c] = []
            return True



        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
        


