import numpy as np

def entropy_node(y):
    if len(y) == 0:
        return 0.0

    total = len(y)

    classes, counts = np.unique(y,return_counts=True)
    proportion = counts/total

    entropy = -np.sum(proportion * np.log2(proportion)) 
    return float(entropy)

    pass

y=[1,1,1,1]
entropy_node(y)
y=[0,1,0,1]
entropy_node(y)