"""Transformación de datos desde data/raw hacia data/processed."""


def transform():
    pass


if __name__ == "__main__":
    transform()

import pandas as pd
import os

df = pd.read_parquet('data/raw/sales.parquet')
result = df.groupby('producto')['venta'].sum().reset_index()

print(result.head())

os.makedirs('data/processed', exist_ok=True)
result.to_parquet('data/processed/sales_summary.parquet')