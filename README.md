
```
hadoop jar C:\Users\ducpa\Desktop\PhanTichDuLieuLon\NaiveBayes.jar NaiveBayesTrainJob -D num_mappers="3" -D num_reducers="1" -D delimiter="," -D input="/diabetes-input/diabetes.csv" -D output="/outputdiabetes-testing" -D continousVariables="1,2,3,4,5,6,7,8" -D targetVariable="9" -D numColumns="9"
```

```
hadoop jar C:\Users\ducpa\Desktop\PhanTichDuLieuLon\NaiveBayes.jar NaiveBayesTestJob -D num_mappers="5" -D num_reducers="1" -D delimiter="," -D input="/diabetes-input/diabetes.csv" -D output="/outputdiabetes-test" -D continousVariables="1,2,3,4,5,6,7,8" -D discreteVariables="" -D targetVariable="9" -D numColumns="9" -D modelPath="/outputdiabetes-testing" -D targetClasses="positive,negative"
```