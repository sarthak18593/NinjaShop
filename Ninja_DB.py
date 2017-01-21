
# coding: utf-8

# In[1]:

import pymongo


# In[2]:

from pymongo import MongoClient
client = MongoClient()


# In[3]:

client = MongoClient('mongodb://localhost:27017/')


# In[4]:

db = client.test_database


# In[5]:

collection = db.test_collection


# In[7]:

posts = db.posts


# In[ ]:

post = [{"item": "Coconut Milk","section": "Canned & Packaged Foods", "X":4, "Y":1 ,"Aisle":"A","Shelf":"1"},
        {"item": "Baguette/French Bread","section": "Bakery, Breakfast, Cereal", "X":2, "Y":2 ,"Aisle":"B","Shelf":"3"},
        {"item": "Frozen Fruit","section": "Frozen Foods", "X":3, "Y":3 ,"Aisle":"C","Shelf":"1"},
        {"item": "Produce","section": "Apples, Gala, bag", "X":3, "Y":4 ,"Aisle":"D","Shelf":"2"},
        {"item": "Beef Stew Meat","section": "Refrigerated Foods", "X":2, "Y":5 ,"Aisle":"E","Shelf":"1"},
        {"item": "Aluminum Foil","section": "Miscellaneous Kitchen Items", "X":4, "Y":6 ,"Aisle":"E","Shelf":"1"},
        {"item": "Milk","section": "Beverages", "X":4, "Y":7 ,"Aisle":"F","Shelf":"2"},
        {"item": "Yellow Mustard","section": "Canned & Packaged Foods", "X":3, "Y":1 ,"Aisle":"A","Shelf":"2"},
        {"item": "Salad Dressing","section": "Canned & Packaged Foods", "X":2, "Y":1 ,"Aisle":"A","Shelf":"1"},
        {"item": "White Bread/Toast, enriched","section": "Bakery, Breakfast, Cereal", "X":3, "Y":2 ,"Aisle":"B","Shelf":"2"}]


# In[ ]:

result= posts.insert_many(post)


# In[ ]:




# In[ ]:




# In[ ]:



