class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def __iter__(self):
        def i_iter(n):
            return reduce(lambda acc, x: acc + i_iter(n), n.child, [n.root()])
        yield self.root()
        for node in i_iter(self):
            yield node

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, i):
        return self.child[i]

    def num_children(self):
        return len(self.child)

t = Tree(2)
t.add_child(Tree(3))
t.add_child(Tree(4))
t.ith_child(0).add_child(Tree(5))
[x for x in t]
