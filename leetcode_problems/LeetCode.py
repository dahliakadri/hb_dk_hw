def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        for num_index, num in enumerate(nums):
            i = num_index + 1
            while i < len(nums):
                if num + nums[i] == target:
                    return [num_index, i]
                i += 1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 17

print(twoSum(nums, target))