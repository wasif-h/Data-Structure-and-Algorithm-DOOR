# singly Linked List all problems
# wasif hossain - DSA

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:

    def __init__(self):
        self.head = None

    def traversal(self):

        print()

        if self.head is None:
            print("Empty Linked List")
        else:

            temp_node = self.head
            while temp_node is not None:

                print(temp_node.data, end=" ")
                temp_node = temp_node.next

    def insert_at_beginning(self, data):

        new_node = Node(data)
        # first correct the reference
        new_node.next = self.head
        # correct the head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        temp_node = self.head  # indicate n1

        while temp_node.next is not None:  # untill n4.next is not none
            temp_node = temp_node.next

        temp_node.next = new_node

    def insert_at_specific_position(self, data, position):
        new_node = Node(data)

        temp_node = self.head

        for i in range(1, position-1):  # already in node 1
            temp_node = temp_node.next

        new_node.next = temp_node.next
        temp_node.next = new_node

    def deletion_at_beginning(self):

        temp_node = self.head
        self.head = temp_node.next
        temp_node.next = None

    def deletion_at_end(self):

        prev = self.head  # n1 , did this to reach the before node of end node
        temp = self.head.next  # n2

        while temp.next is not None:
            prev = prev.next
            temp = temp.next

        prev.next = None

    def deletion_at_specific_position(self, position):

        prev = self.head
        temp = self.head.next  # This will be deleted

        for i in range(1, position-1):
            prev = prev.next
            temp = temp.next

        prev.next = None
        prev.next = temp.next


s1 = SinglyLL()

node1 = Node(8)
node2 = Node(5)
node3 = Node(2)
node4 = Node(1)

s1.head = node1

node1.next = node2
node2.next = node3
node3.next = node4

s1.traversal()  # before
# test any function here
s1.deletion_at_specific_position(2)

s1.traversal()  # after
