class Solution:
    '''
    given a input array of integers, return true if the count 
    (create a dictionary to keep track)if any key already exists
    if this is not the case, return False
    - initialize the dictionary such that each value for the key is at 1
    increments as its running


    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = num
        return False