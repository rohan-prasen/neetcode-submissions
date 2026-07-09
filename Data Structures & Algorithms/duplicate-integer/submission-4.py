class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size  = len(nums)
        dup = set(nums)
        if len(dup) == size: return False
        return True