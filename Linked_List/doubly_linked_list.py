# doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def forward_traversal(self):

        # 5 7 9 11 13
        print()
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def backward_traversal(self):

        # 5 7 9 11 13
        print()

        temp = self.head
        while temp.next is not None:
            # while temp.next because temp should not be updated as none at the end
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.prev

    def insert_at_beginning(self, data):

        # 5 7 9 11 13

        new_node = Node(data)
        temp = self.head

        temp.prev = new_node
        new_node.next = temp
        self.head = new_node

    def insert_at_end(self, data):
        # 5 7 9 11 13
        new_node = Node(data)
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        new_node.prev = temp
        temp.next = new_node

    def insert_at_specific_position(self, data, position):
        # 5 7 9 11 13
        new_node = Node(data)
        temp = self.head

        for i in range(1, position-1):
            temp = temp.next

        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node

    def delete_at_beginning(self):
        # 5 7 9 11 13

        temp = self.head
        self.head = temp.next
        temp.next.prev = None
        temp.next = None

    def delete_at_end(self):
        # 5 7 9 11 13

        before = self.head
        temp = before.next

        while temp.next is not None:
            before = before.next
            temp = temp.next

        before.next = None
        temp.prev = None

    def delete_at_specific_position(self, position):
        # 5 7 9 11 13

        before = self.head
        temp = before.next

        for i in range(1, position-1):
            before = before.next
            temp = temp.next

        before.next = temp.next
        temp.next.prev = before
        temp.prev = None
        temp.next = None


s1 = DoublyLL()

node1 = Node(5)
node2 = Node(7)
node3 = Node(9)
node4 = Node(11)
node5 = Node(13)

s1.head = node1

# forward
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# backward
node5.prev = node4
node4.prev = node3
node3.prev = node2
node2.prev = node1

s1.forward_traversal()

s1.delete_at_specific_position(4)

s1.forward_traversal()
