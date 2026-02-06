class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set() #seen
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)   # () for the function   [] for indexing 
        return False
