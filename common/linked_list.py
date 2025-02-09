class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
  
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return 

            prev.next = cur_node.next
            cur_node = None
    
    def move_tail_to_head(self):
        # Check to see if the linked list has a head node and the head node has a following node
        if self.head and self.head.next:
            # Initialize last variable to store the last node
            last = self.head
            # Initialize the second to last var in None, we will store the second to last node here so we can set its next to None
            second_to_last = None
            # Repeat until next is None, meaning the last member of the linkewd list
            while last.next:
                # On each iteration, we change the second to last var to the current last node and the last variable we then update to next to advance the iteration
                second_to_last = last
                last = last.next
            # Once we are in the last element, we set the head node as the next value of the last node, which we will now update the linked list and set as its new head, former head is now effectively second oelement, 
            last.next = self.head
            second_to_last.next = None
            self.head = last

