class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies_set = set(supplies)
        recipes_d = {}
        for recipe, ingredient in zip(recipes, ingredients):
            recipes_d[recipe] = ingredient
            
        
        memo = {}
        def recr(target):
            if target in memo:
                if memo[target] == -1:
                    memo[target] = False
                return memo[target]
            
            if target not in memo:
                memo[target] = -1
            
            for ingredient in recipes_d[target]:
                if not ((ingredient in supplies_set) or (ingredient in recipes_d and recr(ingredient))):
                    memo[target] = False
                    return False
                
            memo[target] = True
            return True
               
        ans = []
        for recipe in recipes:
            if recr(recipe):
                ans.append(recipe)
        return ans
