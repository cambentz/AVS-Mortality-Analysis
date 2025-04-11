import pandas as pd
from io import StringIO

# Load the raw .txt file with alternative encoding due to special characters
file_path = "../data/raw/AVS_Dryad.txt"
with open(file_path, "r", encoding="shift_jis", errors="replace") as f:
    lines = f.readlines()

# Step 1: Combine multi-line header (lines 1 to 13 after the title line)
header_lines = lines[1:14]
header_combined = ''.join(header_lines).replace('\n', ' ').replace('"', '').strip()

# Step 2: Split into clean column names
column_names = [col.strip() for col in header_combined.split('\t') if col.strip()]

# Step 3: Extract data rows (starting from line 14 onward)
data_lines = lines[14:]
data_str = ''.join(data_lines)

# Step 4: Convert to DataFrame
data_df = pd.read_csv(StringIO(data_str), sep='\t', header=None, names=column_names, engine='python')

# Step 5: Export to CSV
output_path = "../data/raw/AVS_Dryad.csv"
data_df.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")