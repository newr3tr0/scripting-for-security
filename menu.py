import os # interface which allows us to access the underlying is functionality
          

def shutdown():
    os.system("shutdown /s /t 1")# makes use of shell script i.e write command to os


def restart():
    os.system("shutdown /r /t 1")

def menu(): #use function that can be called from anywhere within your program
    print("Please choose from the following options:")
    print("1. Shutdown Computer")
    print("2. Restart Computer")
    print("3. Exit Program")


loop = True

while loop:
    menu() # call menu function
    choice = int(input("Enter Choice: 1/2/3: "))
    if choice == 1:
        print("You have chosen to shutdown your computer....", shutdown())
    elif choice == 2:
        print("You  have chosen to restart your computer...", restart())
    elif choice == 3:
        print("You have chosen to exit the program. Goodbye!")
        loop = False
    else:
        print("Invalid Choice. Please try again.")