import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Tips Dataset Analysis', fontsize=16, fontweight='bold')

ax1 = axes[0, 0]
for sex in tips['sex'].unique():
    sex_data = tips[tips['sex'] == sex]
    ax1.scatter(sex_data['total_bill'], sex_data['tip'], label=sex, alpha=0.6, s=50)
ax1.set_xlabel('Total Bill ($)')
ax1.set_ylabel('Tip ($)')
ax1.set_title('Total Bill vs. Tip (by Sex)')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2 = axes[0, 1]
day_order = ['Thur', 'Fri', 'Sat', 'Sun']
sns.boxplot(data=tips, x='day', y='total_bill', order=day_order, ax=ax2, palette='Set2')
ax2.set_xlabel('Day of Week')
ax2.set_ylabel('Total Bill ($)')
ax2.set_title('Total Bill Distribution per Day')
ax2.grid(True, alpha=0.3, axis='y')

ax3 = axes[1, 0]
sns.histplot(data=tips, x='tip', hue='time', kde=True, ax=ax3, palette='husl', bins=15)
ax3.set_xlabel('Tip ($)')
ax3.set_ylabel('Frequency')
ax3.set_title('Tip Distribution by Time (Lunch/Dinner)')
ax3.legend(title='Time')

ax4 = axes[1, 1]
sns.barplot(data=tips, x='day', y='tip', order=day_order, ax=ax4, palette='Set1', errorbar='ci')
ax4.set_xlabel('Day of Week')
ax4.set_ylabel('Average Tip ($)')
ax4.set_title('Average Tip per Day (with 95% CI)')
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('tips_analysis.png', dpi=300, bbox_inches='tight')
print("Figure saved as 'tips_analysis.png'")
plt.show()