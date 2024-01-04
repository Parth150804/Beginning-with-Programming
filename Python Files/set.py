class Set:
    def __init__(self, elements=[]):
        self.elements = list(set(elements))

    def intersection(self, other_set):
        return Set([elem for elem in self.elements if elem in other_set.elements])

    def union(self, other_set):
        return Set(self.elements + [elem for elem in other_set.elements if elem not in self.elements])

    def difference(self, other_set):
        return Set([elem for elem in self.elements if elem not in other_set.elements])

    def __str__(self):
        return str(self.elements)


