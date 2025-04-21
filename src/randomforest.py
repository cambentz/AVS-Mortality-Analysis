import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
filePath = "../data/processed/DataSheet_2_cleaned.csv"
data = pd.read_csv(filePath)

# make upa and dpa 1 or 0
data['Diagnosis(PA)'] = LabelEncoder().fit_transform(data['Diagnosis(PA)'])

# create data training
x = data.drop(columns=['Diagnosis(PA)'])
y = data['Diagnosis(PA)']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)

y_prediction = model.predict(x_test)
y_probabilty = model.predict_proba(x_test)[:, 1]

# show highest impact 
feuture_importance = pd.Series(model.feature_importances_, index = x.columns)
plt.figure(figsize=(15,10))
sns.barplot(x = feuture_importance, y=feuture_importance.index)
plt.title("Random Forest")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()