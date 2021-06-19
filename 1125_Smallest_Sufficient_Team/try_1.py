class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dp = collections.defaultdict(list)
        dp[frozenset()] = []
        
        for i, skills in enumerate(people):
            people_set = frozenset(skills)
            
            for old_set in list(dp.keys()):
                new_set = old_set.union(people_set)
                if new_set not in dp or len(dp[new_set]) > len(dp[old_set]) + 1:
                    dp[new_set] = dp[old_set] + [i]
        
        return dp[frozenset(req_skills)]