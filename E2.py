class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            node2 = self.head
            while node2.next:
                node2 = node2.next
            node2.next = newnode

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def reverse_elemant(self):
        tmp = self.head
        prev = None
        while tmp is not None:
            next_node = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next_node
        current_node = prev
        print("The reverse node is:")
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print("")

    def middle_elemant(self):
        counter = 0
        tmp = self.head
        while tmp is not None:
            counter += 1
            tmp = tmp.next
        tmp = self.head
        if counter % 2 == 0:
            middle = int(counter / 2)
        else:
            middle = int(counter / 2) + 1
        for i in range(0, middle - 1):
            tmp = tmp.next
        return tmp.data


def cycle_linked_list(head):
    p1 = head
    p2 = head.next
    while p2 and p2.next is not None:
        if p1 == p2:
            return True
        p1 = p1.next
        p2 = p2.next.next
    return False


linked_list = LinkedList()
linked_list.append(11)
linked_list.append(20)
linked_list.append(50)
linked_list.append(84)
linked_list.append(10)
linked_list.append(18)
linked_list.append(90)
linked_list.display()

print("The middle element of a linked list is: ")
print(linked_list.middle_elemant())
new_list = LinkedList()
linked_list.reverse_elemant()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node1

print(" Linked list has a cycle:", cycle_linked_list(node1))