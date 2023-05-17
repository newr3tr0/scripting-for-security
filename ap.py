"assessment program"
"date of completion 12/05/2023"
"made by sam dalgleish"


import os
import socket
import time
import nmap
from rich.progress import Progress, SpinnerColumn, TimeRemainingColumn
import getpass


# Define the regUsers class
class regUsers:
    def __init__(self, userN, passW):
        self.username = userN
        self.password = passW


# Function to login the user
def login():
    # Set the username and password
    USERNAME = "Sentinel"
    PASSWORD = "Sentinel"

    # Create a user object with the given username and password
    user1 = regUsers(USERNAME, PASSWORD)

    # Set the number of login attempts to 0
    attempts = 0

    # Begin a loop that allows the user to attempt to log in 3 times
    while attempts < 3:
        # Ask the user for their username and password
        uName = input("Please enter a username: ")
        pWord = getpass.getpass("Please enter a password: ")

        # Use the Rich library to display a progress spinner for 3 seconds
        with Progress(
            SpinnerColumn(),  # Use a spinner to indicate progress
            TimeRemainingColumn(),  # Display the time remaining in the progress bar
            "{task.completed}/{task.total} completed",  # Display the progress as a fraction
            transient=True,  # The progress bar should disappear after completion
        ) as progress:
            task = progress.add_task(
                "Logging in...", total=3
            )  # Set up a task with a duration of 3 seconds
            for i in range(3):
                time.sleep(1)  # Wait for 1 second
                progress.update(
                    task, advance=1
                )  # Update the progress bar with the current task progress

        # If the username and password are correct, log the user in and exit the loop
        if uName == user1.username and pWord == user1.password:
            print("Access Granted")
            break
        # If the username or password is incorrect, inform the user and increment the login attempts
        else:
            print("Password or username incorrect")
            attempts += 1

        # If the user has used up all their login attempts, inform them and exit the program
        if attempts == 3:
            print("You have used up all tries ")
            exit()


# Function to get the IP address of a host name entered by the user
def get_ip_address():
    hostname = input("Enter the host name you wish to look up: ")
    try:
        ip_address = socket.gethostbyname(hostname)
        print("IP address of", hostname, "is:", ip_address)
        return ip_address

    except socket.gaierror:
        # Handle the socket.gaierror exception and print a message saying the host name could not be resolved
        print("Could not resolve host name:", hostname)
        exit()


# Function to ping an IP address and check if the server is up
def ping_server(ip_address):
    # Use the system ping command with a timeout of 1 second and redirect the output to a null device to suppress it
    response = os.system("ping -n 1  " + ip_address + " > /dev/null 2>&1")
    # If the ping is successful, print a message saying the server is up
    if response == 0:
        print("Server is up!")
    # Otherwise, print a message saying the server is down
    else:
        print("Server is down!")
        exit()


# Main Menu function
def main_menu():
    while True:
        print("\n-------------------------")
        print("Welcome to the Main Menu!")
        print("-------------------------")
        print("Please choose from the following options:")
        print("1. Get IP address and ping server")
        print("2. Shutdown/Restart computer")
        print("3. Run Nmap scan")
        print("4. Exit program")

        # Get user input for the main menu choice
        try:
            choice = int(input("Enter choice (1/2/3/4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Call the appropriate function based on the user's choice
        if choice == 1:
            ip_address = get_ip_address()
            ping_server(ip_address)
        elif choice == 2:
            shutdown_restart_menu()
        elif choice == 3:
            runPortScan()  # Call the function to run Nmap scan
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# both of these are the functions needed to shutdown or restart the computer
def shutdown():
    os.system("shutdown /s /t 1")  # makes use of shell script i.e write command to os


def restart():
    os.system("shutdown /r /t 1")


def runPortScan():
    host = "127.0.0.1"
    nm = nmap.PortScanner()
    nm.scan(host, "21-400")

    print(nm.command_line())  # Print the Nmap command line used to run the scan

    for host in nm.all_hosts():
        print("----------------------------------------------------")
        print("Host : %s (%s)" % (host, nm[host].hostname()))
        print("State : %s" % nm[host].state())

        for protocol in nm[host].all_protocols():
            print("----------")
            print("Protocol : %s" % protocol)

            portList = nm[host][protocol].keys()
            for port in portList:
                print(
                    "port : %s\tstate : %s" % (port, nm[host][protocol][port]["state"])
                )


# Sub-menu function for shutdown/restart options
def shutdown_restart_menu():
    while True:
        print("\n-------------------------------")
        print("Welcome to the Shutdown/Restart Menu!")
        print("-------------------------------")
        print("Please choose from the following options:")
        print("1. Shutdown computer")
        print("2. Restart computer")
        print("3. Back to Main Menu")

        # Get user input for the shutdown/restart menu choice
        try:
            choice = int(input("Enter choice (1/2/3): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Call the appropriate function based on user's choice
        if choice == 1:
            print("You have chosen to shutdown your computer....", shutdown())
        elif choice == 2:
            print("You have chosen to restart your computer...", restart())
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")


# Call the main menu function to start the program
login()
main_menu()
