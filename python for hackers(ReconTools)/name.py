#Create a program that can take input of the users name
#Save the name in a variable
#pass the variable through a function and print "Hello __________"

username = input("Enter your name: ")


def printName(username):
    print("Hello {}".format(username))

printName(username)
