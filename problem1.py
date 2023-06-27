class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self, value):
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node   
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data," ->",end=" ")
            temp=temp.next    
    def atend(self,value):
        print("vijay")
        new_node=Node(value)
        temp=self.head
        while temp.next is not None:
             print("vpjay")
             
             temp=temp.next
             print(temp,temp.next)
        if temp.next is None:
            print(temp.next)
            print("vijay")   
            temp.next=new_node


                  


LL=Linkedlist()
LL.insert(1)  
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.traverse()
LL.atend(5)
LL.traverse()

