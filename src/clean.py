import pandas as pd
import numpy as np
import os

# Define input and output paths
input_dir = "../data/raw"
output_dir = "../data/processed"
os.makedirs(output_dir, exist_ok=True)

# Define helper to clean numeric columns
def clean_numeric(series):
    return pd.to_numeric(series.astype(str).str.replace(r"[^\d.-]", "", regex=True), errors='coerce')

# Condensed column names for AVS_Dryad specifically
avs_dryad_renames = {
    'Patients': 'PatientID',
    'Diagnosis': 'Diagnosis(PA)',
    'Therapy': 'Therapy',
    'Age (y)': 'Age',
    'Gender': 'Gender',
    'SBP (mmHg)': 'SBP',
    'DBP (mmHg)': 'DBP',
    'PRA (ng/ml/h)': 'PRA',
    'PAC (pg/ml)': 'PAC',
    'ARR': 'ARR',
    'K (mEq/L)': 'K',
    'Urinay  aldosterone  (μg/day)': 'Urine_ALD',
    'ARR after 50 mg  captopril loading': 'ARR-50mg',
    'PRA after furosemide  standing test': 'PRA-FST',
    'PAC after saline  load test': 'PAC-SLT',
    'PAC reduction rate after saline infusion test (%)': 'PAC reduction',
    'LI before ACTH stimulation': 'LI-preACTH',
    'LI after ACTH stimulation': 'LI-postACTH',
    'CSI before ACTH stimulation': 'CSI-preACTH',
    'CSI after ACTH stimulation': 'CSI-postACTH',
    'PAC on APA side before ACTH stimulation': 'PAC-APA-preACTH',
    'PAC on contralateral side before ACTH stimulation': 'PAC-CL-preACTH',
    'PAC on APA side after ACTH  stimulation': 'PAC-APA-postACTH',
    'PAC on contralateral side after ACTH stimulation': 'PAC-CL-postACTH',
    'KCNJ5': 'KCNJ5',
    'ATP1A1': 'ATP1A1',
    'ATP2B3': 'ATP2B3',
    'CACNA1D': 'CACNA1D',
    'Antihypertensive agents at diagnosis': 'Anti-agents',
    'Antihypertensive agents after treatment': 'Anti-agents-post',
    'SBP ater surgery (mmHg)': 'SBP-post',
    'DBP after surgery (mmHg)': 'DBP-post'
}

mutation_cols = ["KCNJ5", "ATP1A1", "ATP2B3", "CACNA1D"]

# Loop through all CSV files in the raw data folder
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        print(f"Cleaning {filename}...")
        df = pd.read_csv(os.path.join(input_dir, filename))
        
        # Rename columns for AVS_Dryad file only
        if "AVS_Dryad" in filename:
            df.rename(columns=avs_dryad_renames, inplace=True)
            
        # Drop excluded column from AVS_Dryad
        if "AVS_Dryad" in filename:
            df = df.iloc[:-1]
            
        # Drop mutation columns entirely for now
        df.drop(columns=[col for col in mutation_cols if col in df.columns], inplace=True)

        # Identify other numeric-looking columns and clean them (ND, '<', '>')
        for col in df.columns:
            if df[col].dtype == object:
                try:
                    cleaned = clean_numeric(df[col])
                    if cleaned.notna().sum() > 0:
                        df[col] = cleaned
                except Exception:
                    continue

        # Fill missing numeric values with mean, round only if decimal places exist
        numeric_cols = df.select_dtypes(include='number').columns
        for col in numeric_cols:
            if df[col].isnull().sum() > 0:
                mean_val = df[col].mean()
                filled_mask = df[col].isnull()
                df.loc[filled_mask, col] = mean_val.round(1)
        
        # If all values in the column are whole numbers, convert to Int64 (Age, Gender, ID, etc)
        if df[col].dropna().apply(lambda x: x == int(x)).all():
            df[col] = df[col].astype('Int64')
        
        # Fill missing categorical values with mode
        object_cols = df.select_dtypes(include='object').columns
        for col in object_cols:
            if df[col].isnull().sum() > 0:
                mode_val = df[col].mode(dropna=True)
                if not mode_val.empty:
                    df[col] = df[col].fillna(mode_val[0])

        # Save cleaned file
        base, ext = os.path.splitext(filename)
        cleaned_filename = f"{base}_cleaned{ext}"
        output_path = os.path.join(output_dir, cleaned_filename)
        df.to_csv(output_path, index=False)
        print(f"Saved cleaned file to {output_path}\n")