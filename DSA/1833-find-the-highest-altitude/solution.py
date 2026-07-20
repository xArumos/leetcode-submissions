class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        peak = 0

        for c in gain:
            height += c
            peak = max(peak, height)
        
        return peak
