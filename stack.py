from node import Node

class Stack:
    def __init__(self, name, limit=1000):
        self.name = name
        self.limit = limit
        self.head = None
        self.size = 0

    def has_space(self):
        return self.limit > self.size

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get_name(self):
        return self.name
    
    def peek(self):
        if self.get_size() > 0:
            return self.head.get_value()
        else: return None

    def push(self, value):
        if self.has_space():
            new_head = Node(value)
            old_head = self.head
    
            new_head.set_next_node(old_head)

            self.head = new_head
            self.size += 1
        else: print("This stack is already full.")


    def pop(self):
        if self.get_size() > 0:
            old_head = self.head
            
            self.head = self.head.get_next_node()
            self.size -=1

            return old_head.get_value()
        else: print("This stack is already empty.")

    def list_all_values(self):
        values = []
        pointer = self.head

        while pointer:
            values.append(pointer.get_value())
            pointer = pointer.get_next_node()
        
        return values

    



    