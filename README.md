# Covid Mortality Risk Factors – CSC487 Group Project

## Contributors

- [@Khadi Badiane](https://github.com/khadib12)
- [@Cameron Bentz](https://github.com/cambentz)  
- [@Joey Henry](https://github.com/josephhenry123)  
- [@Luke Lynch](https://github.com/lukelynch10)  

---

## Project Overview

This project analyzes COVID-19 mortality data in connection with key metabolic syndrome factors, including:

- Visceral obesity  
- Hypertension  
- Insulin resistance  
- Dyslipidemia  
- Hyperglycemia  

Our goal is to identify patterns, correlations, and potential predictive indicators of mortality using:

- Real-world patient data  
- Epidemiological datasets from government and research sources  
- Python for data handling and visualization  
- R for extended statistical analysis  

---

## Data Sources

The project draws data from:

- [TanmoyX COVID-19 Patient Precondition Dataset (Kaggle)](https://www.kaggle.com/datasets/tanmoyx/covid19-patient-precondition-dataset/data)  
- [Aniket0712 COVID with Diabetes and Hypertension Dataset (Kaggle)](https://www.kaggle.com/datasets/aniket0712/covid-with-diabetes-and-hypertension-death-counts)  
- [Johns Hopkins University COVID-19 Data Repository (GitHub)](https://github.com/CSSEGISandData/COVID-19)  

These are stored locally in the `data/raw/` directory once downloaded.

---

## Setup Instructions

### 1. Clone the repository

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Kaggle API key

1. Log in to your Kaggle account  
2. Go to: https://www.kaggle.com/settings  
3. Scroll down to the **API** section and click **"Create New API Token"**  
4. This will download a file named `kaggle.json`  
5. Move `kaggle.json` to the following location on your system:

**For Windows:**

```bash
C:\Users\<your-username>\.kaggle\kaggle.json
```

**For macOS/Linux:**

```bash
~/.kaggle/kaggle.json
```

---

## Download the Data

Run the following script to automatically download and organize all datasets into `data/raw/`:

```bash
python src/data_download.py
```

This will:

- Download and extract both Kaggle datasets  
- Clone the Johns Hopkins GitHub repository  
- Organize everything into:

```
data/raw/mexico-govt
data/raw/hypertension
data/raw/johns-hopkins
```

Once the download is complete (can take up to 25 minutes), manually delete the /tmp directory.

---

## License

This project is for educational purposes only and uses publicly available datasets from Kaggle and GitHub.