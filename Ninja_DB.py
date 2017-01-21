
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


# In[6]:

posts = db.posts


# In[7]:

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


# In[8]:

result= posts.insert_many(post)


# In[9]:

import pprint


# In[10]:

pprint.pprint(posts.find_one({"item": "Yellow Mustard"}))


# In[11]:

posts.find_one({"item": "Coconut Milk"})["X"]


# In[12]:

def get_coordinates (item_names):
    x_list = []
    y_list = []
    t=0
    for i in item_names:
        x_list.append(posts.find_one({"item":i})["X"])
        y_list.append(posts.find_one({"item":i})["Y"])
    my_list=list(zip(x_list,y_list))
    return my_list


# In[13]:

get_coordinates(["Coconut Milk", "Yellow Mustard"])


# In[29]:

def path_define (x1,x2):
    if ( min((x1+x2-2),(10-x1-x2))==(x1+x2-2)): #take left path
        return 1
    else :
        return 0

def distance (p1,p2):
    x1,y1=p1
    x2,y2=p2
    if (y1==y2): #horizental motion
        dist= abs(x1-x2)
    elif (x1==x2 and (x1==1 or x1==5) ): # vertical motion
        #this code could be optimized to consider case for a bigger number but for simiplicty we consider the base case only
        dist = abs(y1-y2)
    elif (path_define(x1,x2)==1):#left path
        dist = (x1+x2-2)+ abs (y1-y2)
    elif (path_define(x1,x2)==0): #right path
        dist = (10-x1-x2)+ abs (y1-y2)
    return dist


# In[ ]:




# In[95]:

def shortest_path (mylist):
    if (len(mylist)==1):
        return mylist
    distlist=[]
    for i in range(1,len(mylist)):
        distlist.append((mylist[i],distance(mylist[0],mylist[i])))
    mindist=distlist[0][1]
    x=0
    for d in range(len(distlist)):
        if (mindist>distlist[d][1]):
            x=d
            mindist=distlist[d][1]
    mylist[1], mylist[x+1]=distlist[x][0],mylist[1]
    return mylist[0:1]+shortest_path(mylist[1:])


# In[96]:

print(shortest_path([(5,1),(3,3),(4,1),(1,2)]))


# In[84]:

list=[1,2,3,4]
print(list[2:3])
print(list+list[2:3])


# In[ ]:



