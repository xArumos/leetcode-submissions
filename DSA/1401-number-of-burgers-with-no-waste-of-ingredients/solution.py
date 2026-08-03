class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        j = (tomatoSlices - (2 * cheeseSlices)) // 2
        s = (cheeseSlices - j)
        if tomatoSlices % 2 == 1 or tomatoSlices < cheeseSlices * 2 or s < 0 or j < 0:
            return []
        else:
            return [j, s]
