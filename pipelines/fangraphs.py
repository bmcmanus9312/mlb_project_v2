


# PACKAGE IMPORTS

from pathlib import Path
import pandas as pd

# DIRECTORY SETUP

BASE_DIR = Path(__file__).resolve().parents[1]

print(BASE_DIR)

RAW_DIR = BASE_DIR / 'data' / '00_raw'
OUT_DIR = BASE_DIR / 'data' / '01_interim'

print(RAW_DIR)

# FANGRAPHS FILES

FANGRAPHS_DIR = RAW_DIR / 'fangraphs'

batting_files = sorted(FANGRAPHS_DIR.glob('*batting*.csv'))
pitching_files = sorted(FANGRAPHS_DIR.glob('*pitching*.csv'))

print('Fangraphs Batting Files:')
for file in batting_files:
    print(file.name)

print('Fangraphs Pitching Files:')
for file in pitching_files:
    print(file.name)

batting_df = None
pitching_df = None

keys = ['MLBAMID', 'Season', 'Team']

for file in batting_files:
    df = pd.read_csv(file)

    if batting_df is None:
        batting_df = df
        continue

    # Remove columns already present, except merge keys
    overlapping = df.columns.intersection(batting_df.columns).difference(keys)
    df = df.drop(columns=overlapping)

    batting_df = batting_df.merge(
        df,
        on=keys,
        how='outer'
    )

print(batting_df.shape)
print(batting_df.columns)

for file in pitching_files:
    df = pd.read_csv(file)

    if pitching_df is None:
        pitching_df = df
        continue

    # Remove columns already present, except merge keys
    overlapping = df.columns.intersection(pitching_df.columns).difference(keys)
    df = df.drop(columns=overlapping)

    pitching_df = pitching_df.merge(
        df,
        on=keys,
        how='outer'
    )

print(pitching_df.shape)
print(pitching_df.columns)

batting_df.to_csv(OUT_DIR / 'fangraphs_batting_combined.csv', index=False)
print(f'Combined Fangraphs Batting dataset saved to {OUT_DIR / 'fangraphs_batting_combined.csv'} \n Dataset Shape: {batting_df.shape}')

pitching_df.to_csv(OUT_DIR / 'fangraphs_pitching_combined.csv', index=False)
print(f'Combined Fangraphs Pitching dataset saved to {OUT_DIR / 'fangraphs_pitching_combined.csv'} \n Dataset Shape: {pitching_df.shape}')