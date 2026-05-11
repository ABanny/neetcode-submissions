class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        duplicate = False
        for a, n in enumerate(nums):
            if a > 0:
                if nums[a] == nums[a-1]:
                    duplicate = True
                    break

        return duplicate
            

            