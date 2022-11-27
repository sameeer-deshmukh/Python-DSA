class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" %self.data
    
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list

        Takes O(n) time
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Add new node containing data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or 'None' if not found

        Takes O(n) time
        """

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, position):
        """
        Inserts a new node containing data at index position
        Insertion takes O(1) time but finding the node at the
        insertion point takes O(n) time.
        """

        if position == 0:
            self.add(data)
        else:
            new_node = Node(data)
            prev_node = self.head
            next_node = prev_node.next_node

            while position > 1:
                prev_node = prev_node.next_node
                next_node = prev_node.next_node
                position -= 1

            prev_node.next_node = new_node
            new_node.next_node = next_node
            


    def remove(self, key):
        """
        
        """
        prev_node = None
        current = self.head
        while current:
            if current.data == key and current == self.head:
                self.head = current.next_node
                return True
            elif current.data == key:
                prev_node.next_node = current.next_node
                return True
            else:
                prev_node = current
                current = current.next_node
        return False

    
    def removeAt(self, position):
        """
        
        """
        current_node = self.head
        while position > 0:
            current_node = current_node.next_node
            position -= 1
        
        self.remove(current_node.data)


    def __repr__(self):
        nodes = []
        current = self.head

        while current: 
            if current == self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node == None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)
            current = current.next_node

        return '-> '.join(nodes)