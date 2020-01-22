# def twoSum(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """ 
#         for num_index, num in enumerate(nums):
#             i = num_index + 1
#             while i < len(nums):
#                 if num + nums[i] == target:
#                     return [num_index, i]
#                 i += 1

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        dict_one = {}
        for i, n in enumerate (nums):
            if dict_one.get(target-n) != None:
                return [dict_one[target-n], i]
            else:
                dict_one[n] = i

print(twoSum(nums, target))