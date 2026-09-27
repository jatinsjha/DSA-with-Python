class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if i != j:
                        result.append(i)
                        result.append(j)
        length = len(result)
        result = result[0:(length/2)]
        return result