#!/usr/bin/env python
# coding: utf-8

# # IMPORT LIBRARIES

# In[123]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[124]:


#LOADING THE DATASETS


# In[125]:


df=pd.read_csv('hotel_bookings.csv' )


# In[126]:


#EXPLOTARY DATA ANALYSIS AND DATA CLEANING


# In[127]:


df.head()


# In[128]:


df.tail()


# In[129]:


df.shape


# In[130]:


df.columns


# In[131]:


df.info()


# In[132]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[133]:


df.describe(include='object')


# In[134]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[135]:


df.isnull().sum()


# In[136]:


df.drop('agent',axis=1,inplace=True)
df.drop('company',axis=1,inplace=True)


# In[141]:


df.isnull().sum()



# In[86]:


df.describe()


# In[142]:


df.dropna()


# In[87]:


df=df[df['adr']<5000]


# # ANALYSIS AND VISUALIZATION

# In[143]:


cancelled_perc=df['is_canceled'].value_counts(normalize=True)
print(cancelled_perc)


# In[144]:


plt
plt.title('Reservation status count')
plt.bar(['NOT canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.7)
plt.show()


# In[145]:


plt.figure(figsize=(8,4))
axl=sns.countplot(x='hotel',hue='is_canceled',data=df,palette='Blues')
legend_labels,_=axl.get_legend_handles_labels()

plt.title("Reservation status to differnt hotels",size=20)
plt.xlabel("hotel")
plt.ylabel("number of reservations")
plt.show()


# In[146]:


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[147]:


city_hotel=df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[148]:


resort_hotel=resort_hotel.groupby("reservation_status_date")[['adr']].mean()
city_hotel=city_hotel.groupby("reservation_status_date")[['adr']].mean()


# In[149]:


plt.figure(figsize=(20,8))
plt.title("Average rate in Resort and City hotel",fontsize=30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label="Resort Hotel")
plt.plot(city_hotel.index,city_hotel['adr'],label="City Hotel")
plt.legend(fontsize=20)
plt.show()


# In[150]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
ax1=sns.countplot(x='month',hue='is_canceled',data=df,palette='bright')
legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title("Reservation status per month", size=20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[162]:


plt.figure(figsize=(15, 8))
plt.title('ADR PER MONTH', fontsize=30)
sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.legend(fontsize=20)
plt.show()                        
                                  
                                  


# In[165]:


canceled_data=df[df[is_canceled]==1]
top_10_country=canceled_data


# In[ ]:





# In[ ]:




