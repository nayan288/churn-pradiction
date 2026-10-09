import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

churn_data = pd.read_csv("churndata.csv")

new_data = churn_data['SubscriptionType'].unique()

churn_data["new_contract_length"] = churn_data['ContractLength'].map({
    "Monthly":0, "Quarterly":1, "Annual":2
})

churn_data["new_SubscriptionType"] = churn_data['SubscriptionType'].map({
    "Basic":0,"Standard":1,"Premium":2
})

churn_data["new_Gender"] = churn_data["Gender"].map({
    "Female":0,"Male":1
})

# print(new_data)

churn_data.to_csv("new_data.csv",index=False)

f = churn_data[["Age",'Tenure','UsageFrequency',"SupportCalls","PaymentDelay","TotalSpend","LastInteraction","new_contract_length","new_SubscriptionType","new_Gender"]]
t = churn_data["Churn"] 

model = RandomForestClassifier()

model.fit(f,t)
joblib.dump(model, "model.joblib", compress=3)

data= np.array([[4,35,9,12,5,17,232,18,1,2]])
result= model.predict(data)

print(result)
