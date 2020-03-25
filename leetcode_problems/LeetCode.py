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


#test for one edit
word_one = "tesat"
word_two = "tesats"

word_three = "asta"
word_four = "ask"

word_five = "sets"
word_six = "test"

def one_edit(word_one, word_two):
    test_set = {word_one, word_two}
    #if words are same then auto return false
    if len(test_set) == 1:
        return False
    len_word_one = len(word_one)
    len_word_two = len(word_two)
    difference = abs(len_word_one - len_word_two)
    #if words are different than more than 1 character in length auto return false
    if difference > 1:
        return False
    else:
    #going to loop through each word and check if each letter at the same index is the same. if it is not then I add a count to the edit count. As soon as it goes above 1 then I return false. If I have one at the end then I return true. 
        if len_word_one == len_word_two:
            edit_count = 0
            i = 0
            for letter in word_one:
                if edit_count > 1:
                    return False 
                if letter != word_two[i]:
                    edit_count += 1
                i += 1
            return True

        elif len_word_one > len_word_two:
            edit_count = 0
            i = 0
            for letter in word_one:
                if i <= (len_word_two - 1):
                    if edit_count > 1:
                        return False 
                    if letter != word_two[i]:
                        edit_count += 1
                else:
                    edit_count += 1
                    if edit_count > 1:
                        return False
                    else:
                        return True
                i += 1
            return True

        elif len_word_one < len_word_two:
            edit_count = 0
            i = 0
            for letter in word_two:
                if i <= (len_word_one - 1):
                    if edit_count > 1:
                        return False
                    if letter != word_one[i]:
                        edit_count += 1
                else:
                    edit_count += 1
                    if edit_count > 1:
                        return False
                    else:
                        return True
                i += 1
        
            return True



print(one_edit(word_one, word_two))
print(one_edit(word_three, word_four))
print(one_edit(word_five, word_six))

print(one_edit("ask", "asta"))