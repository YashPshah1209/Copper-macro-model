"""
Run this once to scaffold the project directory structure
and copy the raw LME CSV into data/raw/.
"""

import os
import shutil

DIRS = [
    "data/raw",
    "data/processed",
    "notebooks",
    "scripts",
]

for d in DIRS:
    os.makedirs(d, exist_ok=True)
    print(f"  created  {d}/")

# Rename/copy the investing.com file into the standard raw location
SRC = "Copper Futures Historical Data.csv"
DST = "data/raw/lme_copper.csv"

if os.path.exists(SRC) and not os.path.exists(DST):
    shutil.copy(SRC, DST)
    print(f"  copied   {SRC}  ->  {DST}")
elif os.path.exists(DST):
    print(f"  exists   {DST}  (skipped)")
else:
    print(f"  WARNING  '{SRC}' not found — place it in data/raw/lme_copper.csv manually")

print("\nProject structure ready.")
