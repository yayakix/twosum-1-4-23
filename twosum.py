class Solution(object):
    def twoSum(self, nums, target):
        # slow method
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i and nums[i] + nums[j] == target:
                    return i,j
# faster method
class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            currVal = target - nums[i]
            if map.has_key(currVal):
                return i,map[currVal]
            else:
                map[nums[i]] = i
