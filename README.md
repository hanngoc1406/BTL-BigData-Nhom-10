# Cách thực hiện

- Bước 1: Clone repository
```
git clone https://github.com/hanngoc1406/BTL-BigData-Nhom-10.git

cd BTL-BigData-Nhom-10
```

- Bước 2: Chạy file NaiveBayes.py
```
py NaiveBayes.py
```

- Bước 3: Tạo thư mục đầu vào trong hdfs
```
hdfs dfs -mkdir /diabetes-input
```

- Bước 4: Đẩy file diabetes_hadoop.csv vào folder diabetes-input vừa tạo
```
hadoop fs -put diabetes_hadoop.csv /diabetes-input
```

- Bước 5: Chạy chương trình Training/Test bộ dữ liệu
```
hadoop jar NaiveBayes.jar NaiveBayesTrainJob -D num_mappers="3" -D num_reducers="1" -D delimiter="," -D input="/diabetes-input/diabetes_hadoop.csv" -D output="/outputdiabetes-train" -D continousVariables="1,2,3,4,5,6,7,8" -D targetVariable="9" -D numColumns="9"
```

```
hadoop jar NaiveBayes.jar NaiveBayesTestJob -D num_mappers="5" -D num_reducers="1" -D delimiter="," -D input="/diabetes-input/diabetes_hadoop.csv" -D output="/outputdiabetes-test" -D continousVariables="1,2,3,4,5,6,7,8" -D discreteVariables="" -D targetVariable="9" -D numColumns="9" -D modelPath="/outputdiabetes-train" -D targetClasses="0,1"
```