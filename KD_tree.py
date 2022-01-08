import pandas as pd
from binarytree import tree, Node
from math import floor


class KD_Tree:
    def __init__(self, data):
        self.data = data
        self.tree = None

    def _build(self, points, depth):
        k = len(points.columns)
        _axis = depth % k
        _column = points.columns[_axis]
        if len(points) == 0:
            return None
        objects_list = points.sort_values(by=[_column], ascending=True)
        if len(objects_list) % 2 == 0:
            median_idx = int((len(objects_list) / 2))
        else:
            median_idx = floor((len(objects_list) / 2))

        node = Node(int(round(objects_list.iloc[median_idx][_column], 3)))
        node.left = self._build(objects_list.iloc[0:median_idx], depth + 1)
        node.right = self._build(objects_list.iloc[median_idx + 1:], depth + 1)

        return node

    def build(self):
        self.tree = self._build(self.data, depth=0)


test_df = pd.DataFrame(data=[[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]], columns=['X', 'Y'])
KD = KD_Tree(test_df)
KD.build()
print(KD.tree)
