#!/usr/bin/python3
"""
implementing Nodes and linked lists singly in python
"""


class Node:
    """
    Class that represents a node
    """

    def __init__(self, data, next_node=None):
        """
        initiation instance with private attribute
        Args:
            - data: should be of a value integer otherwise error
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__next = next_node
        self.__data = data

    @property
    def data(self):
        """Property returns Data"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for property data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next(self):
        """Property returns next_node"""
        return self.__next

    @next.setter
    def next(self, value):
        """Setter function for next_node"""
        self.__next = value


class SinglyLinkedList:
    """Class that representes a linked list"""

    def __init__(self):
        """ Initiation instance and it's attributes """
        self.__head = None

    def sorted_insert(self, value):
        """ Adds node at right position """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data >= new_node.data:
            new_node.next = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next and new_node.data > current.next.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def __str__(self):
        """Prints the entire list in stdout"""
        nodes = []
        current = self.__head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "\n".join(nodes)
