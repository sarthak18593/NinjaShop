
# coding: utf-8

# In[7]:

# %load Ninja_DB.py


import pymongo
from PIL import Image, ImageDraw


from pymongo import MongoClient
client = MongoClient()

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database

collection = db.test_collection

posts = db.posts

post = [{"item": "Coconut Milk","section": "Canned & Packaged Foods", "X":4, "Y":1 ,"Aisle":"A","Shelf":"1"},
        {"item": "Bread","section": "Bakery, Breakfast, Cereal", "X":4, "Y":2 ,"Aisle":"B","Shelf":"3"},
        {"item": "Frozen Fruit","section": "Frozen Foods", "X":3, "Y":3 ,"Aisle":"C","Shelf":"1"},
        {"item": "Apples","section": "Produce", "X":4, "Y":3 ,"Aisle":"C","Shelf":"2"},
        {"item": "Beef Stew Meat","section": "Refrigerated Foods", "X":2, "Y":4 ,"Aisle":"D","Shelf":"1"},
        {"item": "Aluminum Foil","section": "Miscellaneous Kitchen Items", "X":4, "Y":5 ,"Aisle":"E","Shelf":"1"},
        {"item": "Milk","section": "Beverages", "X":2, "Y":1 ,"Aisle":"A","Shelf":"2"},
        {"item": "Yellow Mustard","section": "Canned & Packaged Foods", "X":4, "Y":3 ,"Aisle":"C","Shelf":"2"},
        {"item": "Salad Dressing","section": "Canned & Packaged Foods", "X":3, "Y":3 ,"Aisle":"B","Shelf":"1"},
        {"item": "Toast","section": "Bakery, Breakfast, Cereal", "X":2, "Y":2 ,"Aisle":"B","Shelf":"2"}]

posts.delete_many({})
result= posts.insert_many(post)


def get_coordinates (item_names):
    global list_all
    x_list = []
    y_list = []
    aisle=[]
    t=0
    for i in item_names:
        x_list.append(posts.find_one({"item":i})["X"])
        y_list.append(posts.find_one({"item":i})["Y"])
        aisle.append(posts.find_one({"item":i})["Aisle"])
    my_list=list(zip(x_list,y_list))
    list_all=list(zip(my_list,item_names,aisle))
    return my_list



# In[ ]:




# In[8]:

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
#print(shortest_path([(5,1),(1,3),(3,6),(2,3)]))


# In[ ]:




# In[9]:

im = Image.open('GroceryStoreFinal.jpg')#Draw line
draw = ImageDraw.Draw(im)
def draw_line(a,b):
    x1,y1=a
    x2,y2=b
    xd1=x1*65
    yd1=y1*50
    xd2=x2*65
    yd2=y2*50
    if (y1==y2): #horizental motion
        draw.line((yd1,xd1, yd2,xd2), fill=250,width=10)
    elif (x1==x2 and (x1==1 or x1==5) ): # vertical motion
        #this code could be optimized to consider case for a bigger number but for simiplicty we consider the base case only
        draw.line((xd1,yd1, xd2,yd2), fill=250,width=10)
    elif (path_define(x1,x2)==1):#left path
        draw.line((yd1,xd1, yd1,65), fill=250,width=10)
        draw.line((yd1,65,yd2,65), fill=250,width=10)
        draw.line((yd2,65 ,yd2,xd2), fill=250,width=10)
    elif (path_define(x1,x2)==0): #right path
        draw.line((yd1,xd1,yd1,325), fill=250,width=10)
        draw.line((yd1,325,yd2,325), fill=250,width=10)
        draw.line((yd2,325, yd2,xd2), fill=250,width=10)

# In[8]:

def draw_graph(mylist):
    for i in range(len(mylist)-1):
        draw_line(mylist[i],mylist[i+1])
#lista=get_coordinates(["Apples","Bread","Beef Stew Meat"])
#lista=get_coordinates(["Beef Stew Meat","Bread","Apples"])





# In[10]:

def main(mylist):
    ordered_list = []
    lista=get_coordinates(mylist)
    mlist=[(5,1)]+lista
    liste=shortest_path(mlist)
    for i in liste[1:]:
        for j in range(len(list_all)):
             if (i==list_all[j][0]):
                ordered_list.append(list_all[j])
    draw_graph(liste)
    im.show()
    return ordered_list


# In[11]:

#main(["Beef Stew Meat","Bread","Apples"])


# In[12]:



# In[ ]:




# In[ ]:
