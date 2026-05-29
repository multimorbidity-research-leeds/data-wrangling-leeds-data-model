import pandas as pd
from pathlib import Path
import re

def clean(name):
    return re.sub(r'[<>:"/\\|?*]', '_', str(name)).strip()

# Load Excel
df = pd.read_excel(r"C:\Users\hssean\OneDrive - University of Leeds\Desktop\LIDA\ICB- MLTC\Github\Diagnosis codes\msk_codes.xlsx")
print(df.columns)

BASE_DIR = Path("MSK")

grouped = df.groupby(["inflammation_type", "category"])


for (infl_type, category), group in grouped:
    folder = BASE_DIR / str(infl_type)
    folder.mkdir(parents=True, exist_ok=True)

    file_path = folder / f"{category}.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"{'Coding System':<20} {'Code':<15} {'Condition':<80}\n")
        f.write("=" * 90 + "\n")

        for _, row in group.iterrows():
            f.write(f"{row['coding_system']:<20} {row['code']:<15} {row['condition']:<80}\n")

print("Done")

print(df[['coding_system', 'code', 'condition']].head(10))
