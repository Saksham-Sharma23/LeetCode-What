class Node:
    def __init__(self , data = None , next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self , data):
        node = Node(data , self.head)
        self.head = node

    
    def insert_at_end(self, data):
        if self.head is None:
            self.head  = Node(data, None)
            return
        
        itr = self.head 
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        count = 0 
        if self.head == None:
            return count
        
        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count
    

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Cannot remove element")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_values(self , datalist):
        self.head = None
        for data in datalist :
            self.insert_at_end(data)


    def insert_at(self , data ,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Cannot insert")
        if index == 0 :
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            itr = itr.next 
            count += 1
        


        

    def print(self):
        if self.head == None:
            print("Empty")
            return
        
        itr = self.head
        while itr:
            print(itr.data , "->", end = "")
            itr = itr.next

        print(None, "\n")


ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(10)
ll.insert_at_end(1)
ll.insert_at_end(100)
ll.print()
ll.insert_values([1,2,3,4,5,6,7,8,9])
ll.print()
ll.insert_at(55, 6)
ll.print()
