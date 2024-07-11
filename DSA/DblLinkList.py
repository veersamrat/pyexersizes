class Node:
    def __init__(self,priv=None,data=None,next=None):
        self.priv=priv
        self.data=data
        self.next=next

class DblLinkedList:
    def __init__(self):
        self.head=None
    
    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
            
    def print(self):
        if self.head is None:
            print("Double Linked list is empty")
            return
        itr = self.head
        llstr=""
        while itr:
            llstr +=str(itr.data) + "<--->"
            itr=itr.next
        print(llstr)
        
    def insert_bigin(self,data):
        node=Node(None,data,self.head)
        self.head.priv = node
        self.head=node
    
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(None,data,None)
            return
        
        itr = self.head
        while itr.next:
            itr =itr.next
        itr.next = Node(itr,data,None)
    
    def insert_vals(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)
    
    def insert_pos(self,data,pos):
        if pos < 0 or pos >= self.get_len():
            raise Exception("Invalid posistion")
        if pos == 0:
            self.insert_bigin(data)
            return
        countr = 0
        itr = self.head
        while itr:
            if countr == pos-1:
                data_node = Node(itr,data,itr.next)
                itr.next=data_node
                break
            countr += 1
            itr = itr.next
    
    def insert_aftr_val(self,data,data_aftr):
        itr = self.head
        while itr:
            if itr.data == data_aftr:
                data_node = Node(itr,data,itr.next)
                itr.next=data_node
                break
            itr = itr.next
            
    def remove_at(self,pos):
        if pos < 0 or pos >= self.get_len():
            raise Exception("Invalid posistion")
        if pos == 0:
            self.head = self.head.next
            self.head.priv = None
            return
        countr = 0
        itr = self.head
        while itr:
            if countr == pos-1:
                itr.next = itr.next.next
                break
            countr += 1
            itr = itr.next
            
    def remove_val(self,rm_data):
        countr = 0
        itr = self.head
        while itr:
            if itr.data == rm_data:
                self.remove_at(countr)
                break
            countr += 1
            itr = itr.next

    