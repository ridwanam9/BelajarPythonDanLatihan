class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # last / curret node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def insert_at_position(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current_node = self.head
        position = 0
        while current_node and position < index - 1:
            current_node = current_node.next
            position += 1
        if not current_node:
            print("Index not present")
            return
        new_node.next = current_node.next
        current_node.next = new_node


    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")



lists = Linked_list()
lists.insert_at_end(10)
lists.insert_at_end(20)
lists.insert_at_end(30)
lists.insert_at_beginning(0)
lists.insert_at_end(40)
lists.insert_at_position(2, 60)
lists.print_list()