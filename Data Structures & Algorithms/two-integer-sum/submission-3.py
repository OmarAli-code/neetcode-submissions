class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        for l in range (len(nums)-1):

            for r in range(l+1,len(nums)):
                sum = nums[l] + nums[r] 

                if sum == target:
                    return [l,r]
            
            

            
        return None
