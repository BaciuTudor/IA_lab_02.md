import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')

print("=== Dimensiunea și tipurile de date ===")
print(f"Dimensiune: {tips.shape}")
print(f"\nTipuri de date:\n{tips.dtypes}")
print(f"\nStatistici descriptive:\n{tips.describe()}")

print("\n=== Bacșis mediu per zi ===")
avg_tip_day = tips.groupby('day').agg({'tip': 'mean'})
print(avg_tip_day)

print("\n=== Bacșis mediu per sex ===")
avg_tip_sex = tips.groupby('sex').agg({'tip': 'mean'})
print(avg_tip_sex)

tips_copy = tips.copy()
tips_copy['procent_bacsis'] = (tips_copy['tip'] / tips_copy['total_bill']) * 100

print("\n=== Primele 5 rânduri cu noua coloană ===")
print(tips_copy.head())

print("\n=== Cele mai generoase 5 mese ===")
top_5_generous = tips_copy.nlargest(5, 'procent_bacsis')[['total_bill', 'tip', 'procent_bacsis']]
print(top_5_generous)

print("\n=== Mese servite per zi și per categorie de fumători ===")
meals_per_day_smoker = tips.groupby(['day', 'smoker']).size().reset_index(name='count')
print(meals_per_day_smoker)