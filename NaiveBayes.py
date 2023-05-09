import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix,accuracy_score, roc_auc_score,roc_curve, classification_report,mean_squared_error,f1_score,recall_score,precision_score

# Load dữ liệu
dataset = pd.read_csv("diabetes.csv")

# Xử lý dữ liệu và thay giá trị 0 
dataset['Glucose'] = dataset['Glucose'].replace(0, dataset['Glucose'].mean()) #normal distribution
dataset['BloodPressure'] = dataset['BloodPressure'].replace(0, dataset['BloodPressure'].mean()) #normal distribution
dataset['SkinThickness'] = dataset['SkinThickness'].replace(0, dataset['SkinThickness'].median()) #skewed distribution
dataset['Insulin'] = dataset['Insulin'].replace(0, dataset['Insulin'].median()) #skewed distribution
dataset['BMI'] = dataset['BMI'].replace(0, dataset['BMI'].median()) #skewed distribution
dataset.to_csv('temp.csv')

# Chia dữ liệu thành tập train và test với tỉ lệ 80:20
X_train, X_test, y_train, y_test = train_test_split(dataset.drop('Outcome', axis=1), dataset['Outcome'], test_size=0.2, random_state=0)

# Khởi tạo mô hình Naive Bayes
nb = GaussianNB()

# Huấn luyện mô hình trên tập huấn luyện
nb.fit(X_train, y_train)

# Dự đoán kết quả trên tập kiểm tra
y_pred = nb.predict(X_test)

# Tính độ chính xác của mô hình
accuracy = accuracy_score(y_test, y_pred)
print("NUMBER OF UNIQUE VALUES:\n")
print(dataset.nunique())
print("Độ chính xác:", accuracy*100)

# Xuất file csv cho hadoop
hadoopdataset = pd.read_csv("temp.csv")
hadoopdataset.to_csv('Test_2.csv', index=False)
os.remove('temp.csv')
print(hadoopdataset)
