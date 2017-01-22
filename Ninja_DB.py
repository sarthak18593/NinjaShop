
# coding: utf-8

# In[55]:

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
        {"item": "Baguette/French Bread","section": "Bakery, Breakfast, Cereal", "X":2, "Y":2 ,"Aisle":"B","Shelf":"3"},
        {"item": "Frozen Fruit","section": "Frozen Foods", "X":3, "Y":3 ,"Aisle":"C","Shelf":"1"},
        {"item": "Apples, Gala, bag","section": "Produce", "X":3, "Y":4 ,"Aisle":"D","Shelf":"2"},
        {"item": "Beef Stew Meat","section": "Refrigerated Foods", "X":2, "Y":5 ,"Aisle":"E","Shelf":"1"},
        {"item": "Aluminum Foil","section": "Miscellaneous Kitchen Items", "X":4, "Y":6 ,"Aisle":"E","Shelf":"1"},
        {"item": "Milk","section": "Beverages", "X":4, "Y":7 ,"Aisle":"F","Shelf":"2"},
        {"item": "Yellow Mustard","section": "Canned & Packaged Foods", "X":3, "Y":1 ,"Aisle":"A","Shelf":"2"},
        {"item": "Salad Dressing","section": "Canned & Packaged Foods", "X":2, "Y":1 ,"Aisle":"A","Shelf":"1"},
        {"item": "White Bread/Toast, enriched","section": "Bakery, Breakfast, Cereal", "X":3, "Y":2 ,"Aisle":"B","Shelf":"2"}]


result= posts.insert_many(post)

def get_coordinates (item_names):
    x_list = []
    y_list = []
    t=0
    for i in item_names:
        x_list.append(posts.find_one({"item":i})["X"])
        y_list.append(posts.find_one({"item":i})["Y"])
    my_list=list(zip(x_list,y_list))
    return my_list


get_coordinates(["Coconut Milk", "Yellow Mustard"])


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


im = Image.open('GroceryStoreFinal.jpg')#Draw line
draw = ImageDraw.Draw(im)


# In[7]:

def draw_line(a,b):
    x1,y1=a
    x2,y2=b
    xd1=x1*65
    yd1=y1*50
    xd2=x2*65
    yd2=y2*50

    if (y1==y2): #horizental motion
        draw.line((yd1,xd1, yd2,xd2), fill=100,width=10)
    elif (x1==x2 and (x1==1 or x1==5) ): # vertical motion
        #this code could be optimized to consider case for a bigger number but for simiplicty we consider the base case only
        draw.line((xd1,yd1, xd2,yd2), fill=100,width=10)
    elif (path_define(x1,x2)==1):#left path
        draw.line((yd1,xd1, yd1,65), fill=100,width=10)
        draw.line((yd1,65,yd2,65), fill=100,width=10)
        draw.line((yd2,65 ,yd2,xd2), fill=100,width=10)
    elif (path_define(x1,x2)==0): #right path
        draw.line((yd1,xd1,yd1,325), fill=100,width=10)
        draw.line((yd1,325,yd2,325), fill=100,width=10)
        draw.line((yd2,325, yd2,xd2), fill=100,width=10)


# In[8]:

def draw_graph(mylist):
    for i in range(len(mylist)-1):
        draw_line(mylist[i],mylist[i+1])

# In[ ]:

samplist = ['Apples, Gala, bag','Baguette/French Bread','Coconut Milk','Salad Dressing','White Bread/Toast, enriched','Milk']
# In[ ]:
samplistlist = get_coordinates(samplist)
print(samplistlist)
list1 = shortest_path(samplistlist)
print(list1)
listy=[(5,1)]
listyyyy= listy+list1
print(listyyyy)
draw_graph(listyyyy)

im.show()

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def lis():
   return render_template('hello.html', name = list1)

if __name__ == '__main__':
   app.run(debug = True)
