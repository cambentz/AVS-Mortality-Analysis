import pandas as pd
import os

# Define input and output paths
input_dir = "../data/raw"
output_dir = "../data/processed"
os.makedirs(output_dir, exist_ok=True)

# Define helper to clean numeric columns
def clean_numeric(series):
    return pd.to_numeric(series.astype(str).str.replace(r"[^\d.-]", "", regex=True), errors='coerce')

# Loop through all CSV files in the raw data folder
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        print(f"Cleaning {filename}...")
        df = pd.read_csv(os.path.join(input_dir, filename))

        # Identify numeric-looking columns and clean them (ND, '<', '>')
        for col in df.columns:
            if df[col].dtype == object:
                try:
                    cleaned = clean_numeric(df[col])
                    if cleaned.notna().sum() > 0:
                        df[col] = cleaned
                except Exception:
                    continue

        # Fill missing numeric values with the column mean
        numeric_cols = df.select_dtypes(include='number').columns
        for col in numeric_cols:
            if df[col].isnull().sum() > 0:
                mean_val = df[col].mean()
                df[col] = df[col].fillna(mean_val).round(1)

        # Save cleaned file
        base, ext = os.path.splitext(filename)
        cleaned_filename = f"{base}_cleaned{ext}"
        output_path = os.path.join(output_dir, cleaned_filename)
        df.to_csv(output_path, index=False)
        print(f"Saved cleaned file to {output_path}\n")