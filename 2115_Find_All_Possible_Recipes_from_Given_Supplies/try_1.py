import collections

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        for recipe, ingredient_list in zip(recipes, ingredients):
            if recipe not in graph:
                graph[recipe] = {'parents': 0, 'children': []}
                
            for ingredient in ingredient_list:
                if ingredient not in graph:
                    graph[ingredient] = {'parents': 0, 'children': []}
                
                graph[ingredient]['children'].append(recipe)
                graph[recipe]['parents'] += 1
        
        recipes_set = set(recipes)
        supplies_set = set(supplies)
        
        que = collections.deque()
        for k, d in graph.items():
            parents = d['parents']
            if parents == 0:
                que.append(k)
        
        ans = []
        while que:
            ele = que.popleft()
            
            if ele in recipes_set:
                ans.append(ele)
                supplies_set.add(ele)
            
            if ele not in supplies_set:
                continue
            
            for child in graph[ele]['children']:
                graph[child]['parents'] -= 1
                if graph[child]['parents'] == 0:
                    que.append(child)
        return ans
