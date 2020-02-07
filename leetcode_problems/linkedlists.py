Given a linked list, return the reverse list
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

Given a linked list, return a linked list of every other node in the list



Given a linked list, return a total of all even nodes added and all off nodes subtracted