class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        # Initialize with a dummy head node (-1)
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # If the list was empty, update tail as well
        if self.tail == self.head:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        # Check for invalid index
        if index < 0:
            return False

        curr = self.head
        i = 0
        
        # Traverse until curr is the node *just before* the target index
        while i < index and curr and curr.next:
            curr = curr.next
            i += 1
            
        # If curr.next is None, the index is out of bounds
        if curr is None or curr.next is None:
            return False
            
        # Node to be deleted
        node_to_remove = curr.next
        
        # Bypass the node
        curr.next = node_to_remove.next
        
        # If we removed the tail node, update the tail pointer
        if node_to_remove == self.tail:
            self.tail = curr
            
        return True

    def getValues(self) -> list[int]:
        # Start at self.head.next to skip the dummy node
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res