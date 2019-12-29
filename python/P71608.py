class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, i):
        return self.child[i]

    def num_children(self):
        return len(self.child)


class Pre(Tree):
    def preorder(self):
        def i_preorder(n):
            return reduce(lambda x, y: x + i_preorder(y), n.child, [n.root()])
        return list(i_preorder(self))
