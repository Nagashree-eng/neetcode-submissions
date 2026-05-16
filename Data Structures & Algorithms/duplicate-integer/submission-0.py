class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for x in nums:
            if  x not in arr:
                arr.append(x)
            else:
                return True
        return False