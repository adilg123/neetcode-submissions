from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for num, count in count.items():
            if count > len(nums) // 3:
                res.append(num)

        return res

