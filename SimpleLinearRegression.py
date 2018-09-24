
# coding: utf-8

# In[69]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
import requests, json
from flask import request

df = pd.read_csv("SalaryData.csv")

train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

df_copy = train_set.copy()

test_set_full = test_set.copy()
test_set = test_set.drop(["Salary"], axis=1)

train_labels = df_copy["Salary"]

train_set_full = train_set.copy()
train_set = train_set.drop(["Salary"], axis=1)

lin_reg = LinearRegression()

lin_reg.fit(train_set, train_labels)

salary_pred = lin_reg.predict(test_set)

salary_pred


# In[70]:


import pickle

with open("python_lin_reg_model.pkl", "wb") as file_handler:
    pickle.dump(lin_reg, file_handler)
    
with open("python_lin_reg_model.pkl", "rb") as file_handler:
    loaded_pickle = pickle.load(file_handler)
    
loaded_pickle


# In[72]:



joblib.dump(lin_reg, "linear_regression_model.pkl")

joblib.dump(train_set, "training_data.pkl")
joblib.dump(train_labels, "training_labels.pkl")


# In[73]:



years_exp = {"yearsOfExperience": 8}

response = requests.post("/predict", json = years_exp)

response.json()


# In[74]:


df_copy.query('YearsExperience > 7 and YearsExperience <= 8')


# In[75]:


data = json.dumps([{"YearsExperience": 12,"Salary": 140000}, 
                   {"YearsExperience": 12.1,"Salary": 142000}])

data


# In[76]:



response = requests.post("{}/retrain".format(BASE_URL), json = data)

response = response.json()


# In[77]:


response = requests.post("{}/predict".format(BASE_URL), json = years_exp)

response = response.json()


# In[78]:


response = requests.get("{}/currentDetails".format(BASE_URL))

response.json()

