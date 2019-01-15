#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

class ListNode:
    def __init__(self, address, data, next):
        self.address = address
        self.data = data
        self.next = next

def nonrecurse(head):
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    h = head
    while cur:
        h = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return h

first_node, n, k = [i for i in input().split()]
node_lst = []
for i in range(int(n)):
    address, data, next = [a for a in input().split()]
    node_lst.append(ListNode(address, data, next))

print(node_lst)