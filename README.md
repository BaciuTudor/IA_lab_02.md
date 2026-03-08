# Laborator 02 IA - NumPy, Pandas, Matplotlib, Seaborn

Acest repository contine cerintele de laborator si tema pentru analiza de date in Python, folosind:

- `NumPy` pentru operatii numerice si matriciale
- `Pandas` pentru manipulare de date tabelare
- `Matplotlib` pentru grafice de baza
- `Seaborn` pentru vizualizari statistice

## Structura proiectului

```text
laborator02IA/
|-- cerinta_3_1_numpy.py
|-- cerinta_3_2_pandas.py
|-- cerinta_3_3_matplotlib.py
|-- cerinta_3_4_seaborn.py
|-- cerinta_3_5_heatmap.py
|-- cerinta_3_6_titanic.py
|-- requirements.txt
|-- README.md
|-- assets/
|   |-- distributii_seaborn.png
|   |-- grafice_iris_matplotlib.png
|   |-- heatmap_corelatie_iris.png
|   |-- iris_pairplot.png
|   |-- iris_violinplots.png
|   |-- tips_analysis.png
|   |-- titanic_analiza.png
`-- tema/
	|-- tema_a_numpy.py
	|-- tema_b_tips.py
	|-- tema_c_dashboard.py
	|-- tema_d_bonus_iris.py
	`-- tema_e_colab.ipynb
```

## Cerinte

- Python `3.10+` (recomandat)
- `pip`

## Instalare

Din radacina proiectului:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Rulare cerinte laborator

```powershell
py .\cerinta_3_1_numpy.py
py .\cerinta_3_2_pandas.py
py .\cerinta_3_3_matplotlib.py
py .\cerinta_3_4_seaborn.py
py .\cerinta_3_5_heatmap.py
py .\cerinta_3_6_titanic.py
```

Scripturile de vizualizare salveaza figuri `.png` (de exemplu: `grafice_iris_matplotlib.png`, `distributii_seaborn.png`, `heatmap_corelatie_iris.png`, `titanic_analiza.png`). In repository, imaginile rezultate sunt stocate in folderul `assets/`.

## Rulare tema

```powershell
py .\tema\tema_a_numpy.py
py .\tema\tema_b_tips.py
py .\tema\tema_c_dashboard.py
py .\tema\tema_d_bonus_iris.py
```

Notebook-ul Google Colab/Jupyter este disponibil in:

- `tema/tema_e_colab.ipynb`

## Ce acopera fiecare fisier

- `cerinta_3_1_numpy.py`: array-uri, statistici, operatii vectorizate, comparatie performanta lista vs NumPy.
- `cerinta_3_2_pandas.py`: explorare si agregare pe dataset-ul `iris`.
- `cerinta_3_3_matplotlib.py`: 4 tipuri de grafice Matplotlib pe `iris`.
- `cerinta_3_4_seaborn.py`: distributii (hist, box, violin) pe `iris` si `tips`.
- `cerinta_3_5_heatmap.py`: matrice de corelatie Pearson + heatmap pentru `iris`.
- `cerinta_3_6_titanic.py`: analiza supravietuirii pe `titanic` (sex/clasa + vizualizari).
- `tema/tema_a_numpy.py`: operatii matriciale, inversa, determinant, verificare matrice identitate.
- `tema/tema_b_tips.py`: analiza descriptiva pe `tips` + procent bacsis.
- `tema/tema_c_dashboard.py`: dashboard 2x2 cu grafice pentru `tips`.
- `tema/tema_d_bonus_iris.py`: pairplot si violinplot pe dataset-ul `iris`.

## Dependinte

Dependintele sunt listate in `requirements.txt`:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`

plus pachetele auxiliare instalate automat (ex: `python-dateutil`, `pillow`, `packaging`).