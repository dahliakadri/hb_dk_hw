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

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 17

# print(twoSum(nums, target))

# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         nums_dict = {}
#         for num in nums:
#             if nums_dict.get(num) == None:
#                 nums_dict[num] = num
#             else:
#                 return True
#         return False


# defclass Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         given a list of numbers rotate the first number right and the last number 
#         to the front of the list, continue this one by one for k amount of times

#         index zero and move it to index 1 then i take the last index and move it
#         to index zero . i repeat this k times


#         while k > 0:
#             nums[1] = nums[0]
#             nums[0] = nums[-1]
#             nums.pop()
#             k = k -1

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        current = head
        a = current.val
        a_node = ListNode(a)
        b = current.next.val
        b_node = ListNode(b)
        b_node.next = a_node
        x = b_node
        current = current.next

        while current.next is not None:
            if b_node is not None:
                b = current.next.val
                b_node = ListNode(b)
                b_node.next = x
                x = b_node
            current = current.next


        print(b_node.val)
        print(b_node.next.val)
        print(b_node.next.next.val)
        print(b_node.next.next.next.val)

       
def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        current = head
        a = current.val
        a_node = ListNode(a)

        if head.next is not None:
            b = head.next.val
            b_node = ListNode(b)
            b_node.next = a_node
            x = b_node
            current = head.next
        else:
            return

        while current.next is not None:
            b = current.next.val
            b_node = ListNode(b)
            b_node.next = x
            x = b_node
            current = current.next
        
        return x



apple_node = ListNode("apple")
berry_node = ListNode("berry")
cherry_node = ListNode("cherry")
rasberry_node = ListNode("rasberry")

apple_node.next = berry_node
berry_node.next = cherry_node
cherry_node.next = rasberry_node

reverseList(apple_node)