import pandas as pd, numpy as np
np.random.seed(42)
rows=200
df=pd.DataFrame({
 "case_id":range(1,rows+1),
 "issue_type":np.random.choice(["Listing Issue","ASIN Merge","Order Defect","Account Health","Policy Clarification"],rows),
 "region":np.random.choice(["NA","EU","FE"],rows),
 "description":np.random.choice(["Missing details","Incorrect info","Seller confusion","Technical failure","Policy unclear"],rows),
 "resolution_time_min":np.random.randint(5,120,rows),
 "escalated":np.random.choice([0,1],rows,p=[0.8,0.2])
})
df.to_csv("data/sample_contact_data.csv", index=False)
print("CSV created.")
