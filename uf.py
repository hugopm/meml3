class Uf:
    def __init__(self, n):
        self.parent_node = [i for i in range(n)]

    def find(self, k):
        if self.parent_node[k] != k:
            self.parent_node[k] = self.find(self.parent_node[k])
        return self.parent_node[k]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.parent_node[x] = y
