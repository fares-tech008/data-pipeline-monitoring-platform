import pandas as pd
from pathlib import Path

# Project root
project_root = Path(__file__).parent.parent

source_file = project_root / "data" / "raw" / "online_retail.csv"
target_file = project_root / "data" / "landing" / "online_retail.csv"

# Read data
df = pd.read_csv(source_file)

print("Dataset loaded successfully")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nColumn Names:")
print(df.columns.tolist())

# Save to landing layer
df.to_csv(target_file, index=False)

print("\nFile copied to landing layer successfully")