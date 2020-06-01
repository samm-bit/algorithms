# element to be placed in the list
class Element(object):
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self, head=None):
        self.head=head

    def append(self, new_element:Element):
        current = self.head
        if self.head!=None:
            self.head = new_element
        else:
            # same as self.head.next
            while current.next: # moves to end of linkedlist 
                current=current.next 
            current.next=new_element # adds the element to the end of the linkedlist
    
    def get_position(self, position:int):
        counter = 1
        current = self.head
        if position < 1: # position = index+1
            return None
        while current and counter <= position:
            if counter == position:
                return current # returns the element at position
            current = current.next
            counter += 1 # moves the pointer along the linkedlist to the next element
        return None

    def insert(self, new_element:Element, position:int):
        counter = 1
        current = self.head
        if position>1:
            while current and counter < position:
                if counter == position - 1: # element before insert
                    new_element.next = current.next # ensure the inserted element has reference to the next element 
                    current.next=new_element # insert the new element
                current=current.next
                counter+=1
        elif position==1:
            new_element.next= self.head
            self.head=new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next: # getting references to elements before and after, ready for deletion
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next