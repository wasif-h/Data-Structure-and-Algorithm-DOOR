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
s1.backward_traversal()
