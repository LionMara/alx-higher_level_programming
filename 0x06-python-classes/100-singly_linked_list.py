#!/usr/bin/python3

"""
class Node  defines a node of a singly linked list
private intsance : data
  * property getter: data
  * property setter: data
       data is integer
private instance: next_node
  * property getter: next_node
  * property setter: next_node
      next_node = None or Node
      next_node is error

"""

class Node:
    """
    class Node  will have only two private instances
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or type(value) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""
class SinglyLinkedList defines a singly linked list
private instance: head
   * no setter or getter needed
prints entire list one node by line

public instance method: sorted_insert
   * Inserts new Node

"""

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __repr__(self):
        temp = self.__head
        total= ""
        while temp:
            total += "{:d}".format(temp.data)
            temp = temp.next_node
            if temp:
                total += "\n"
        return total


    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            curr = self.__head
            prev = None
            while curr and value > curr.data:
                prev = curr
                curr = curr.next_node
            if curr is None:
                prev.next_node = Node(value)
            elif curr is self.__head and prev is None:
                self.__head = Node(value, curr)
            else:
                newest_node = Node(value, curr)
                prev.next_node = newest_node
