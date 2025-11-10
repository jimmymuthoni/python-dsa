from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums:List[int], k: int) -> bool:
        num_idx = {}
        for i in range(len(nums)):
            if nums[i] in num_idx:
                if abs(num_idx[nums[i]] -i) <= k:
                    return True
            num_idx[nums[i]] = i
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))