class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set() #seen表示已经见过的
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)   #遇到没见过的就把它加进去
        return False
