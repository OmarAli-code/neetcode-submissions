class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max = 0
        for l in range(len(prices)):
            for r in range(l+1,len(prices)):
                prof = prices[r]- prices[l]

                if prof > max:
                    max = prof
        
        return max
                