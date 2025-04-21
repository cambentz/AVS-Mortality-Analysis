import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc

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
feature_importance = pd.Series(model.feature_importances_, index = x.columns)
plt.figure(figsize=(15,10))
sns.barplot(x = feature_importance, y=feature_importance.index)
plt.title("Random Forest")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.savefig('../outputs/figures/predictive/RF_histogram.png')
#plt.show()

# Evaluate model
print("Confusion Matrix:\n", confusion_matrix(y_test, y_prediction))
print("\nClassification Report:\n", classification_report(y_test, y_prediction))
print("\nROC AUC Score:", roc_auc_score(y_test, y_probabilty))

# ROC curve and AUC
fpr, tpr, thresholds = roc_curve(y_test, y_probabilty)
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(
    fpr,
    tpr, 
    label=f"Logistic Regression (AUC = {roc_auc:.2f})", 
    color='navy'
    )
plt.plot(
    [0, 1], 
    [0, 1], 
    linestyle='--', 
    color='gray'
    )
plt.title("ROC Curve - APA vs BHA Prediction")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc="lower right")
plt.grid(True)
plt.tight_layout()
plt.savefig('../outputs/figures/predictive/RF_ROC.png')
plt.show()