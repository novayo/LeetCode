
from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_table = {}
        self.rating_table = {}
        self.rank_table = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.rank_table:
                self.rank_table[cuisine] = SortedList()
                
            self.cuisine_table[food] = cuisine
            self.rating_table[food] = rating
            self.rank_table[cuisine].add((-rating, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        ori_rating = self.rating_table[food]
        cuisine = self.cuisine_table[food]
        
        self.rank_table[cuisine].remove((-ori_rating, food))
        self.rank_table[cuisine].add((-newRating, food))
        self.rating_table[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.rank_table[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)