class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        i = j = 0
        
        while (j < len(nums)):
            if nums[i] == nums[j] == 1:
                j += 1
            else:
                maxCount = max(maxCount, (j - i))
                i = j + 1
                j = i
        
        return max(maxCount, (j - i))
