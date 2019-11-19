class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return int(self.rt)

    def ith_child(self, i):
        return self.child[i]

    def num_children(self):
        return len(self.child)


class Pre(Tree):
    def preorder(self):
        def i_preorder(n):
            return list(reduce(lambda x, y: x + i_preorder(y), n.child, [n.root]))
        return i_preorder(self) 

t = Pre(2)
t.add_child(Pre(3))
t.add_child(Pre(4))
print(t.num_children())
t.ith_child(1).add_child(Pre(5))
print(t.preorder())
