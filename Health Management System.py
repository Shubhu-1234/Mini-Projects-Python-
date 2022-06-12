# Health Management System

# Defining the function
def getdate():
    import datetime
    return datetime.datetime.now() #This will print "2022-04-16 18:51:12.312057"
v=getdate()
v=str(v)
"""
def getdate():
    import time
    localtime = time.asctime(time.localtime(time.time()))
    return localtime() #This will print Sun Apr 17 12:10:38 2022
v=getdate()
v=str
"""
#Starting
print("1.Lock\n2.Retrieve")
x=int(input())
print("1.Harry\n2.Rohan\n3.Hammad")
y = int(input())
print("1.Diet\n2.Exercise")
z = int(input())

# This is for harry
if x == 1 and y == 1 and z == 1:
    print("Diet:")
    a = str(input())
    with open("Harry_Diet.txt", "a") as f:
        s = "Time:[{}] Diet:{}\n".format(v, a)
        f.write(s)
        print("You have succesfully Lock the file")

elif x == 1 and y == 1 and z == 2:
    print("Exercise:")
    b = str(input())
    with open("Harry_Exercise.txt", "a") as f:
        r = "Time:[{}] Exercise:{}\n".format(v, b)
        f.write(r)
        print("You have succesfully Lock the file")

elif x == 2 and y == 1 and z == 1:
    with open("Harry_Diet.txt", "r") as f:
        print(f.read())

elif x == 2 and y == 1 and z == 2:
    with open("Harry_Exercise.txt", "r") as f:
        print(f.read())

# This is for Rohan
elif x == 1 and y == 2 and z == 1:
    print("Diet:")
    a = str(input())
    with open("Rohan_Diet.txt", "a") as f:
        s = "Time:[{}] Diet:{}\n".format(v, a)
        f.write(s)
        print("You have succesfully Lock the file")

elif x == 1 and y == 2 and z == 2:
    print("Exercise:")
    b = str(input())
    with open("Rohan_Exercise.txt", "a") as f:
        r = "Time:[{}] Exercise:{}\n".format(v, b)
        f.write(r)
        print("You have succesfully Lock the file")

elif x == 2 and y == 2 and z == 1:
    with open("Rohan_Diet.txt", "r") as f:
        print(f.read())

elif x == 2 and y == 2 and z == 2:
    with open("Rohan_Exercise.txt", "r") as f:
        print(f.read())

# This for Hammad
elif x == 1 and y == 3 and z == 1:
    print("Diet:")
    a = str(input())
    with open("Hammad_Diet.txt", "a") as f:
        s = "Time:[{}] Diet:{}\n".format(v, a)
        f.write(s)
        print("You have succesfully Lock the file")

elif x == 1 and y == 3 and z == 2:
    print("Exercise:")
    b = str(input())
    with open("Hammad_Exercise.txt", "a") as f:
        r = "Time:[{}] Exercise:{}\n".format(v, b)
        f.write(r)
        print("You have succesfully Lock the file")

elif x == 2 and y == 3 and z == 1:
    with open("Hammad_Diet.txt", "r") as f:
        print(f.read())

elif x == 2 and y == 3 and z == 2:
    with open("Hammad_Exercise.txt", "r") as f:
        print(f.read())
else:
    print("Error!Please Try Again!")









