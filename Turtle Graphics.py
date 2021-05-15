# Ninja Twist (Turtle Graphics)
import turtle
ninja = turtle.Turtle()
ninja.speed(10)
for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    ninja.right(2)
turtle.done()

# Python Persistence.
data={'a':'some_value',
      'b':[9,4,7],
      'c':['some_str','another_str','spam','ham'],
      'd':{'key':'nested_dictionary'},
      }

# Store Data
import pickle
file=open('filename','wb') #file object in binary write mode
pickle.dump(data,file) #dump the data in the file object
file.close() #close the file to write into the file

# load data
import pickle
file=open('filename','rb') #file object in binary read mode
data=pickle.load(file) #load the data back
file.close()
print(data)


# Function utility for save and load
import pickle
def save(filename,object):
    file=open(filename,'wb')
    pickle.dump(object,file)
    file.close()
def load(filename):
    file=open(filename,'rb')
    object=pickle.load(file)
    file.close()
    return object
list_object=[1,1,2,3,5,8,'a','e','o','u']
save(list_file, list_object)
new_list=load(list_file)
print(new_list)


