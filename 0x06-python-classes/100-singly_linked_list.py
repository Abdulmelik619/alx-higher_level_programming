class Node:
    def __init__(self, data, next_node=None):
        self.data=data
        self.next_node=next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(data,int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if(not isinstance(value, None) or
                not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head=None

    def sorted_insert(self, value):
        newnode=Node(value)
        if(self.__head==None):
            newnode.next_node=self.__head
            self.__head=newnode
        elif(self.__head.data > value):
            newnode.next=self.__head
            self.__head=newnode
        else:
            a=self.__head
            while(a.self.__next_node != None):
                if(a.self.__next_node.data > value):
                    newnode=Node(value)
                    c=a.self.__next_node
                    a.self.__next_node=newnode
                    break
                a=a.self.__next_node
            
