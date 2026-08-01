class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueList = []
        for num in nums:
            if num not in uniqueList:
                uniqueList.append(num)
            else:
                return True
        
        return False
        