# Data Analytics & Visualization — Note Complete

## 1. Python per Data Analysis

**Stack principale:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

**pandas:**
```python
df = pd.read_csv('dati.csv')
df.head(), df.info(), df.describe()
df.isnull().sum()
df.dropna(), df.fillna(value)
df.groupby('categoria')['valore'].agg(['mean', 'sum', 'count'])
df.merge(df2, on='id', how='left')
df['data'] = pd.to_datetime(df['data'])
```

**numpy:**
```python
arr = np.array([1, 2, 3])
arr.mean(), arr.std(), arr.sum()
np.linspace(0, 10, 100)
np.random.seed(42)
```

## 2. Visualizzazione

**matplotlib:**
```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0,0].plot(x, y, label='Serie')
axes[0,1].bar(categories, values)
axes[1,0].scatter(x, y)
axes[1,1].hist(data, bins=30)
plt.tight_layout()
plt.savefig('chart.png', dpi=300)
```

**seaborn (statistical plots):**
```python
sns.boxplot(x='categoria', y='valore', data=df)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
sns.pairplot(df, hue='target')
sns.violinplot(x='categoria', y='valore', data=df)
```

## 3. Jupyter Notebook

- `jupyter notebook` o `jupyter lab`
- Celle: Code, Markdown, Raw
- `%matplotlib inline` per grafici embedded
- `!comando` per shell
- `.ipynb` formato JSON
- Google Colab: notebook cloud con GPU gratis

## 4. Power Query (Excel / Power BI)

- **ETL**: Extract → Transform → Load
- **M Language**: linguaggio funzionale per transform
- **Operazioni**: merge, append, pivot, unpivot, split column, group by
- **Data source**: file (CSV, Excel, JSON), database, web, API
- **Refresh**: pianificato / manuale

## 5. Statistica Base

| Concetto | Formula/Dettaglio |
|----------|-------------------|
| Media | `sum(x) / n` |
| Mediana | Valore centrale ordinato |
| Deviazione standard | `sqrt(sum((x-μ)²) / n)` |
| Correlazione | Pearson (-1 a +1) |
| Percentile | 25°, 50° (mediana), 75° |
| Distribuzione | normale, uniforme, binomiale |

## 6. Dashboard e Reporting

- **Power BI**: misure DAX, drill-through, slicer, report interattivi
- **Grafana**: time series dashboard (Prometheus, InfluxDB, SQL)
- **Jupyter + Voilà**: notebook → web app interattiva
- **Streamlit**: dashboard Python rapidi (pandas, plotly, maps)

## 7. Data Pipeline

```python
# Pipeline tipica
def extract(path): return pd.read_csv(path)
def transform(df):
    df = df.drop_duplicates()
    df['data'] = pd.to_datetime(df['data'])
    df = df[df['valore'] > 0]
    return df
def load(df, output): df.to_parquet(output)

df = extract('raw.csv')
df = transform(df)
load(df, 'clean.parquet')
```
