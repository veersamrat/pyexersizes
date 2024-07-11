
from SingleLinkList import *
from DblLinkList import *

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert_vals([95,62,6454,45,545,79])
    # ll.print()
    # ll.insert_bigin(95)
    # ll.insert_bigin(20)
    # ll.print()
    # ll.insert_end(95)
    # ll.insert_end(20)
    ll1.print()
    print("Length : ",ll1.get_len())
    ll1.remove_at(2)
    ll1.print()
    ll1.insert_pos(69,2)
    ll1.print()
    ll1.insert_aftr_val(98,69)
    ll1.print()
    ll1.remove_val(98)
    ll1.print()
    
    dll = DblLinkedList()
    dll.insert_vals([95,62,6454,45,545,79])
    dll.print()
    print("Length : ",dll.get_len())
    dll.remove_at(2)
    dll.print()
    dll.insert_pos(69,2)
    dll.print()
    dll.insert_aftr_val(98,69)
    dll.print()
    dll.remove_val(98)
    dll.print()
    
    # ll = LinkedList()
    # ll.insert_vals(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_aftr_val("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_val("orange") # remove orange from linked list
    # ll.print()
    # ll.remove_val("figs")
    # ll.print()
    # ll.remove_val("banana")
    # ll.remove_val("mango")
    # ll.remove_val("apple")
    # ll.remove_val("grapes")
    # ll.print()
    