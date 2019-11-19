class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def __iter__(self):


    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, i):
        return self.child[i]

    def num_children(self):
        return len(self.child)


