import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('Updated_Crop_Recommendation.csv')

print(data.head())
label_encoder = LabelEncoder()
data['Recommended_Crop'] = label_encoder.fit_transform(data['Recommended_Crop'])

X = data.drop('Recommended_Crop', axis=1)
y = data['Recommended_Crop']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
import matplotlib.pyplot as plt

feature_importances = model.feature_importances_
features = X.columns

plt.barh(features, feature_importances)
plt.xlabel("Feature Importance")
plt.title("Feature Importance for Crop Prediction")
plt.show()
import joblib

joblib.dump(model, 'crop_recommendation_model.pkl')

