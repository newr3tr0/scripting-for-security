import time
from rich.progress import Progress, SpinnerColumn, TimeRemainingColumn

# Define the regUsers class
class regUsers:
    def __init__(self, userN, passW):
        self.username = userN
        self.password = passW

# Set the username and password
USERNAME = "sam"
PASSWORD = "Bob"

# Create a user object with the given username and password
user1 = regUsers(USERNAME, PASSWORD)

# Set the number of login attempts to 0
attempts = 0

# Begin a loop that allows the user to attempt to log in 3 times
while attempts < 3:
    # Ask the user for their username and password
    uName = input("Please enter a username: ")
    pWord = input("Please enter a password: ")

    # Use the Rich library to display a progress spinner for 3 seconds
    with Progress(
        SpinnerColumn(),  # Use a spinner to indicate progress
        TimeRemainingColumn(),  # Display the time remaining in the progress bar
        "{task.completed}/{task.total} completed",  # Display the progress as a fraction
        transient=True,  # The progress bar should disappear after completion
    ) as progress:
        task = progress.add_task("Logging in...", total=3)  # Set up a task with a duration of 3 seconds
        for i in range(3):
            time.sleep(1)  # Wait for 1 second
            progress.update(task, advance=1)  # Update the progress bar with the current task progress

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
