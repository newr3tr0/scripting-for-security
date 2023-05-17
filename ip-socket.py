import os
import socket

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
    response = os.system("ping -c 1 -W 1 " + ip_address + " > /dev/null 2>&1")
    # If the ping is successful, print a message saying the server is up
    if response == 0:
        print("Server is up!")
    # Otherwise, print a message saying the server is down
    else:
        print("Server is down!")
        exit()

# Get the IP address of the host name entered by the user
ip_address = get_ip_address()

# Ping the IP address to check if the server is up
ping_server(ip_address)
