# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes_map = dict()
        self.head, self.tail = None, None

    def get(self, key: int) -> int:
        if key not in self.nodes_map:
            return -1

        cur_node = self.nodes_map[key]

        if cur_node.prev:
            cur_node.prev.next = cur_node.next
        if cur_node.next:
            cur_node.next.prev = cur_node.prev

        if self.tail == cur_node and cur_node.prev:
            self.tail = cur_node.prev
        if self.head == cur_node and cur_node.next:
            cur_node.next.prev = cur_node

        if self.head != cur_node:
            cur_node.next, self.head.prev = self.head, cur_node

        cur_node.prev = None
        self.head = cur_node

        return cur_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes_map:
            self.nodes_map[key].val = value
            self.get(key)
        else:
            new_node = Node(key, value)
            self.nodes_map[key] = new_node
            if not self.head:
                self.head, self.tail = new_node, new_node
            else:
                new_node.next, self.head.prev = self.head, new_node
                self.head = new_node
            if len(self.nodes_map) > self.capacity:
                del self.nodes_map[self.tail.key]
                self.tail = self.tail.prev
                self.tail.next = None
