"""Extracción de datos desde la fuente hacia data/raw."""


def extract():
    pass


if __name__ == "__main__":
    extract()

import pandas as pd
import random
import os

data = {
    'producto': [random.choice(['A', 'B', 'C']) for _ in range(10)],
    'venta': [random.randint(50, 100) for _ in range(10)]
}
df = pd.DataFrame(data)
print(df.head())

os.makedirs('data/raw', exist_ok=True)
df.to_parquet('data/raw/sales.parquet')