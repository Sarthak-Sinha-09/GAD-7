#!/usr/bin/env python
# coding: utf-8

# In[229]:


import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[230]:


os.chdir("C:\\Users\\sinha\\OneDrive\Desktop")
data=pd.read_csv("phq_all_final.csv")
data=data.drop(["type"],axis=1) # Droping the type column as it is same throughout.
pt_count=data["patient_id"].nunique()# Calculating the number of patients i.e.15,502


# #### Defining a K.P.I. "RATE"
# Rate is defined as the continuous change of the GAD-7 score over time. A negative rate means that the GAD-7 score is decreasing and the therapy is working. I have measured the efficacy of the therapy on each patient by calculating the number of times the rate was negative and dividing by the total no times the rate was calculated. For instance, if a patient undergoes the therapy for 6 months and the GAD-7 score was calculated 6 times and it was observed that 4 out of 6 times the score decreased from that of the previous month. So, the therapy was successful for about 66% of that patient.

# In[231]:


data['rate'] = data.groupby(['patient_id'])['score'].shift(1)
data['rate'] = data["score"]-data['rate']


# ## Problem :
# We currently have the problem of not being able to visualize progress well for this assessment to mental health providers and their patients.
# 
# ## Solution : 
# It is very difficult to visualize the progress of all the 15,502 patients at the same time. So I have created a user-defined function that takes the patient id as input and returns the success percentage and tracks the change in GAD-7 score over time.

# In[232]:


def patient_analysis():
    
    ID=input("Please enter the patient id: ")
    ID=int(ID)
    data_new=data[data["patient_id"]==ID]
    cnt=data_new["rate"].notnull().sum() #total count
    cnt_n=sum(n < 0 for n in data_new["rate"]) #total negative count
    perc= round((cnt_n/cnt)*100,2)
    data_new['date'] = pd.DatetimeIndex(data_new['date']).date
    data_new["ym"] = data_new["date"].astype(str)
    sns.set(rc={'figure.figsize':(20,12)})
    sns.lineplot(x='ym', y='rate', data=data_new).set_title('Change in GAD-7 score over the period of time')
    print("The therapy was successful for about "+str(perc)+"%")
    return 

    
    


# In[233]:


patient_analysis()# Calling the function to take the patient id as input


# In[217]:





# ### Insights that can be drawn from he data
#  The GAD-7 score of some patients suddenly shoots within a month, even though previously it was dropping on a constant basis. Which means that certain other external factors might be resposible and for this reason that months record can be ignored.
#  
# ### Assumptions
# All the patients are being provided with the same quality of therapy and the efficacy of the therapy does not varies with age or gender. 
# If a patient's current GAD-7 score was recorded to be less than 10 and there is no further score available it is assumed that the patient has recovered from GAD, atleast for a while.
# 
# ### What other information could have been helpful?
# Research says that women are 2 times more sucessiptible to GAD than men, it is more common in young adults. Genetics is also a major factor in contributing towards GAD. So, if the data would have contained information about the sex of the patient and a family history of GAD it would have been helpful in creating a new metric for all the patients that also takes account for these new factors and can be used along with the GAD-7 score during the therapy. Also, if a patient is expereincing a sharp change in his/her GAD-7 score they should be asked further questions that if it was due to some new external factor or not.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Source: https://adaa.org/understanding-anxiety/facts-statistics
# 
# 
# https://www.childrenshospital.org/conditions-and-treatments/conditions/g/generalized-anxiety-disorder-gad#:~:text=Current%20research%20suggests%20that%20one,the%20way%20a%20person%20feels.
# 

# In[ ]:




