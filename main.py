# Pandas ValueError: cannot insert X, already exists

import pandas as pd

df = pd.DataFrame({
    'ID': [1, 2, 3],
    'name': ['Alice', 'Bobby', 'Carl'],
})

df.index.name = 'ID'

print(df)

df = df.reset_index(drop=True)

print('-' * 50)

print(df)