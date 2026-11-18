import pandas as pd
from pathlib import Path



data_path = Path("water_potability.csv")

if not data_path.exists():
    possible_paths = [
        Path("../water_potability.csv"),
        Path("./water_potability.csv"),
        Path("/app/devResources/workspace/water_potability.csv"),
    ]
    for path in possible_paths:
        if path.exists():
            data_path = path
            break

df = pd.read_csv(data_path)
print("DataFrame Loaded")
df.head(5)