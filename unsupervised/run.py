from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("./unsupervised/dataset.csv")
players = list(dataset.pop('player'))

samples = dataset.values

mergings = linkage(samples, method='complete')

dendrogram(mergings,
           labels=players,
           leaf_rotation=90,
           leaf_font_size=6,
           )
plt.show()
