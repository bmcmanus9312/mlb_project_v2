

from pathlib import Path
import pandas as pd

# DIRECTORY SETUP

BASE_DIR = Path(__file__).resolve().parents[1]

print(BASE_DIR)

RAW_DIR = BASE_DIR / 'data' / '00_raw'
OUT_DIR = BASE_DIR / 'data' / '01_interim'

print(RAW_DIR)

# CHADWICK FILES

CHADWICK_DIR = RAW_DIR / 'chadwick'

chadwick_files = sorted(CHADWICK_DIR.glob('people-*.csv'))
assert len(chadwick_files) == 16, f'Missing Chadwick files: {len(chadwick_files)} files found'

print(f'Chadwick files found: {len(chadwick_files)}')

chadwick_df = pd.concat(
    [pd.read_csv(file, low_memory=False) for file in chadwick_files],
    ignore_index=True
)

print(chadwick_df.shape)
print(chadwick_df.columns)

chadwick_df = chadwick_df.drop(
      columns={
          'key_npb', 'key_sr_nfl', 'key_sr_nba', 'key_sr_nhl',
          'death_year', 'death_month', 'death_day',
          'col_played_first', 'col_played_last',
          'pro_managed_first', 'pro_managed_last',
          'mlb_managed_first', 'mlb_managed_last',
          'col_managed_first', 'col_managed_last',
          'pro_umpired_first', 'pro_umpired_last',
          'mlb_umpired_first', 'mlb_umpired_last'
      }
)

chadwick_df.to_csv(OUT_DIR / 'chadwick_combined.csv', index=False)
print(f'Combined Chadwick dataset saved to {OUT_DIR / 'chadwick_combined.csv'} \n Dataset Shape: {chadwick_df.shape}')