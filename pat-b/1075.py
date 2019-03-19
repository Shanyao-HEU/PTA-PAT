class Node:
    def __init__(self, address, data, pnext=None):
        self.address = address
        self.data = data
        self._next = pnext

head, N, K = input().split()
node_lst = []
for i in range(int(N)):
    address, data, pnext = input().split()
    node_lst.append(Node(address, data, pnext))

print(node_lst)
    