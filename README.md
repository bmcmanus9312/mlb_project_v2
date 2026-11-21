# MLB Injury Pricing Project (v2)

**Author:** Brendan McManus

**Written:** 10-21-2026

## 0. Research questions and the two deliverable models

**Q1 — Pricing.**
- Conditional on performance, age, position and market year, do free-agent contracts discount injury history?
- How large is the discount in dollars, and is it larger or smaller than the injury history's actual predictive effect on future production?
- A discount that is too small relative to predictive power is a market inefficiency.

**Q2 — Delivery.**
- Given injury history, does the player produce what the contract pays for?
- Can under-performance be predicted at signing time?
- Two outcomes:
  - a. continuous surplus = value of WAR delivered minus salary paid
  - b. binary under-performance relative to an age-adjusted projection.

These two quesions are linked between the two is the paper's thesis: if injury variables carry weight in Q2 but not in Q1, teams underweight injury risk.


## 1. Target repository structure

```
mlb_project_v2/
├── README.md                     
├── pyproject.toml                
├── .gitignore                    
├── configs/
│   ├── paths.yaml                
│   └── params.yaml               lookbacks, lambda grid, thresholds, eras, base year
├── data/
│   ├── 00_raw/                   
│   │   ├── injuries/        
│   │   ├── contracts/            
│   │   ├── statistics/            
│   │   ├── chadwick/             player register with keys
│   │   └── fred/                 CPI-U annual
│   ├── 01_interim/               
│   ├── 02_processed/             
│   └── 03_model_data/           
├── src/                   
│   ├── config.py                 
│   ├── injuries/                 
│   ├── contracts/                
│   ├── stats/                    
├── pipelines/                    
├── notebooks/                    
├── reports/
│   ├── figures/
│   └── tables/
├── paper/                        
└── docs/                         
```

## Data sources

Raw data is not included in this repository. A `SOURCE.md` will be added to `00_raw/` folders with information regarding source, reproducability, and use policies.

| Source | What it provides | Coverage | Used by | Licence / sharing |
|---|---|---|---|---|
| The Baseball Cube - MLB Injured List History | MLB injured-list data with dates, list type and injury description | 2000 Season to Aug 27, 2026 (detailed from 2012) |  | Purchased; not redistributable |
| Cot's Baseball Contracts (Baseball Prospectus) | Free-agent signings: club, years, guarantee, AAV, options, opt-outs, qualifying offer | 1991–2026 FA signings for all 30 teams | | Fair use for noncommercial research with citation; raw files not redistributed |
| FanGraphs Player Stats | WAR, playing time, batting, pitching and fielding statistics | 2000–2026 seasons, all players | | FanGraphs terms of use; raw exports not redistributed |
| Chadwick Baseball Bureau Register | Player ID crosswalk (MLBAM, FanGraphs, Baseball-Reference, Retrosheet), birth dates, MLB career span | All players |  | ODC-By 1.0; redistribution allowed with attribution |
| FRED, series CPIAUCSL | Consumer price index for inflation adjustment | 1990–2025 annual means |  | Public Data |

