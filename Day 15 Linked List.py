class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        newNode=Node(data)
        if head is None:
            head=newNode
            return head
        else:
            tail=head
            while True:
                if tail.next is None:
                    break
                tail=tail.next
            tail.next=newNode
            return head

mylist= Solution()
