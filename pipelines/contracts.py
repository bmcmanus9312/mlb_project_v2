'''
Purpose:
    Initial cleaning and concat of Cots FA contracts

Inputs:
    00_raw/* FA guarantee.csv"

Outputs:


'''

# PACKAGE IMPORTS

from pathlib import Path
import pandas as pd

# DIRECTORY SETUP

BASE_DIR = Path(__file__).resolve().parents[1]

print(BASE_DIR)

RAW_DIR = BASE_DIR / 'data' / '00_raw'
OUT_DIR = BASE_DIR / 'data' / '01_interim'

print(RAW_DIR)

# CONTRACT FILES

CONTRACTS_DIR = RAW_DIR / 'cots'

contract_files = sorted(CONTRACTS_DIR.glob('* FA guarantee.csv'))
assert len(contract_files) == 30, f'Missing Team FA files: {len(contract_files)} files found'

frames = []

# removes top 4 header rows which are present in csv formatting
for file in contract_files:
    df = pd.read_csv(file, skiprows=4)
    df['team_stem'] = file.stem.split()[0]
    frames.append(df)

contract_df = pd.concat(frames, ignore_index=True)

# remove team totals
contract_df = contract_df[
    ~contract_df['Player']
    .astype('string')
    .str.strip()
    .str.match(r"(?i)^Total(?:\s|$)", na=False)
].reset_index(drop=True)

# confirm files are concatenated
print(contract_df.shape)

print(contract_df.columns)
### RENAME COLS
contract_df.columns = (
    contract_df.columns
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

contract_df = contract_df.rename(
    columns={
        'Player':'player',
        "Pos'n": 'Position',
        'Age':'age',
        'Qual Offer':'qualifying_offer',
        'Old Club':'old_club',
        'New Club':'new_club',
        'Years':'years',
        'Guarantee':'guarantee',
        'Term':'term',
        'Option':'option',
        'Opt Out':'opt_out',
        'Player Agent':'player_agent',
        'Club Owner':'club_owner',
        'Baseball Ops head / club GM':'club_GM_or_OPS_head',
        'Details':'details'
    }
)

print(contract_df.columns)

print(contract_df.isnull().sum())

TEXT_COLS = [
    'Position',
    'qualifying_offer',
    'old_club',
    'new_club',
    'term',
    'option',
    'opt_out',
    'player_agent',
    'club_owner',
    'club_GM_or_OPS_head',
    'details'
    ]

for col in TEXT_COLS:
    if col in contract_df.columns:
        contract_df[col] = (
            contract_df[col]
            .astype('string')
            .str.strip()
        )

'''
NUMERIC_COLS = ['guarantee', 'AAV']

for col in NUMERIC_COLS:
    contract_df[col] = pd.to_numeric(
        contract_df[col]
        .astype('string')
        .str.replace(r"[$,]", "", regex=True),
        errors='coerce'
    )
contract_df["years"] = pd.to_numeric(
    contract_df["years"], errors="coerce"
)

'''

contract_df.to_csv(OUT_DIR / 'cots_merged.csv', index=False)
print(f'{len(contract_df)} contracts in {OUT_DIR / 'cost_merged_csv'}')