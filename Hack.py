# This is my code for reading and storing saved data on a local .txt computer file for our App


# We start by reading the data that is already stored
f = open("hack.txt", "r")
AllTrash = []  # holds all of the instances that the user inputed


class TrashOBJ:
    def __init__(self, n, t, p):
        self.name = n  # string
        self.type = t  # string
        self.image = p  # computer file


# reads all of the data from a file and stores it as instances
next_line = f.readline()
while next_line != "":
    a = f.readline().strip("\n")
    b = f.readline().strip("\n")
    c = f.readline().strip("\n")
    AllTrash.append(TrashOBJ(a, b, c))
    next_line = f.readline()


# This will update based on the information that we read
numRecycle = 0
numFoodwaste = 0
numLandfill = 0

f.close()  # closes the local storage

# At this point, we have opened the local storage file and read the data written on it.
# We now want to take in user input and store it on that data file we just read.


f = open("hack.txt", "w")  # reopens the local storage for writing purposes now

# This is the function that the user input would be plugged into.
# I made this function to process the user input.
# The user input was made with Kivy by one of my friends.
def Ask(n, t, p):
    "Demo for how the user input would be processed, saved into a class, and stored in the local file memory."
    global numRecycle
    global numFoodwaste
    global numLandfill

    location = TrashOBJ(n, t, p)  # makes the data into a class instance

    return location


# Lets do a demo

# First take in user input
n = input()  # input a name
t = input()  # input a type
p = input()  # input a picture (just use a name for now)

AllTrash.append(Ask(n, t, p))  # makes the user input an instance

# these are for display printing purposes on the terminal
for i in range(0, len(AllTrash)):
    print("Trash Piece Number " + ":" + str(i + 1))
    print("    name:", AllTrash[i].name)
    print("    type:", AllTrash[i].type)
    print("    image:", AllTrash[i].image)

# now I am going to itterate through the entire AllTrash list and print the attributes in the local storage
for i in AllTrash:
    f.write("Start\n")
    f.write(i.name + "\n")
    f.write(i.type + "\n")
    f.write(i.image + "\n")
f.close()  # closes the local storage


# when the submit button is released, we want the program to:
# create an instance of OBJ class with current user input
# add this instance into the list
# refresh page(reset)
