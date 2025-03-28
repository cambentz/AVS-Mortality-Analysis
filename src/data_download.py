import os
import time
import kaggle
import shutil
from git import Repo

# Define paths
RAW_DATA_PATH = "./data/raw"
KAGGLE_DATASETS = {
    "tanmoyx/covid19-patient-precondition-dataset": "mexico-govt",
    "aniket0712/covid-with-diabetes-and-hypertension-death-counts": "hypertension"
}
JH_REPO_URL = "https://github.com/CSSEGISandData/COVID-19.git"
JH_TARGET_DIR = os.path.join(RAW_DATA_PATH, "johns-hopkins")
JH_SUBDIR = "csse_covid_19_data"

# Create base raw data directory
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# Function to download Kaggle datasets
def download_kaggle_dataset(dataset_slug, folder_name):
    folder_path = os.path.join(RAW_DATA_PATH, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Downloading {dataset_slug} to {folder_path}...")

    kaggle.api.dataset_download_files(dataset_slug, path=folder_path, unzip=True)

    # Remove zip file if exists
    for file in os.listdir(folder_path):
        if file.endswith(".zip"):
            os.remove(os.path.join(folder_path, file))

# Download all Kaggle datasets
for slug, folder in KAGGLE_DATASETS.items():
    download_kaggle_dataset(slug, folder)

# Clone Johns Hopkins COVID-19 repo and keep only the relevant folder
if not os.path.exists(JH_TARGET_DIR):
    print("Cloning Johns Hopkins repo... This may take some time.")

    tmp_repo_path = "./tmp/tmp_jh_repo"
    start_time = time.time()

    Repo.clone_from(JH_REPO_URL, tmp_repo_path)

    elapsed_time = time.time() - start_time
    print(f"Clone complete. Took {elapsed_time:.1f} seconds.")

    src_path = os.path.join(tmp_repo_path, JH_SUBDIR)
    shutil.move(src_path, JH_TARGET_DIR)
    print("Files moved to johns-hopkins folder, feel free to delete the tmp folder.")
else:
    print("Johns Hopkins data already exists. Skipping clone.")

print("All datasets downloaded successfully.")