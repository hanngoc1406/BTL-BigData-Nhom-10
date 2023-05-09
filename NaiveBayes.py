import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix,accuracy_score, roc_auc_score,roc_curve, classification_report,mean_squared_error,f1_score,recall_score,precision_score

# Load dữ liệu
dataset = pd.read_csv("diabetes.csv")

print("\n \n Dữ liệu trước xử lý \n \n", dataset.head())

# Hiện biểu đồ phân phối
dataset.hist(bins=10,figsize=(10,10))
plt.show()

# Thay giá trị 0 trong một số cột
dataset['Glucose'] = dataset['Glucose'].replace(0, dataset['Glucose'].mean()) # Phân phối chuẩn
dataset['BloodPressure'] = dataset['BloodPressure'].replace(0, dataset['BloodPressure'].mean()) # Phân phối chuẩn
dataset['SkinThickness'] = dataset['SkinThickness'].replace(0, dataset['SkinThickness'].median()) # Phân phối lệch
dataset['Insulin'] = dataset['Insulin'].replace(0, dataset['Insulin'].median()) # Phân phối lệch
dataset['BMI'] = dataset['BMI'].replace(0, dataset['BMI'].median()) # Phân phối lệch

# In dữ liệu sau xử lý
print("\n \n Dữ liệu sau xử lý \n \n", dataset.head(), "\n \n")

# Chia dữ liệu thành tập train và test với tỉ lệ 80:20
X_train, X_test, y_train, y_test = train_test_split(dataset.drop('Outcome', axis=1), dataset['Outcome'], test_size=0.2, random_state=0)

# Khởi tạo mô hình Naive Bayes sử dụng phân phối Gausian
nb = GaussianNB()

# Huấn luyện mô hình trên tập train
nb.fit(X_train, y_train)

# Dự đoán kết quả trên tập kiểm tra
y_pred = nb.predict(X_test)

# Tính độ chính xác của mô hình
accuracy = accuracy_score(y_test, y_pred)
print("\n \n \n \n Độ chính xác:", accuracy*100, "\n \n")

# Xuất file đã được xử lý cho csv cho hadoop
dataset.to_csv('diabetes_hadoop.csv', header=False, index=False)
