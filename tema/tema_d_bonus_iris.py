import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

plt.figure(figsize=(12, 10))
pairplot = sns.pairplot(df, hue='species', diag_kind='kde', height=2.5)
pairplot.figure.suptitle('Iris Dataset - Pairplot with KDE Diagonal', y=1.001, fontsize=16)
plt.savefig('iris_pairplot.png', dpi=300, bbox_inches='tight')
plt.close()

fig, axes = plt.subplots(1, 4, figsize=(16, 5))
features = iris.feature_names

for idx, (ax, feature) in enumerate(zip(axes, features)):
    sns.violinplot(data=df, x='species', y=feature, hue='species', ax=ax, split=False, legend=False)
    ax.set_title(feature.replace('_', ' ').title(), fontsize=12)
    ax.set_xlabel('Species')
    ax.set_ylabel('Value')

fig.suptitle('Iris Dataset - Violinplots by Species', fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig('iris_violinplots.png', dpi=300, bbox_inches='tight')
plt.close()