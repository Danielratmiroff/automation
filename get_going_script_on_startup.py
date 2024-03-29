
# This script will run on bootup. 
# To run this script on bootup, add the following line to your applications startups (Ubuntu: Startup Applications)
# gnome-terminal -- fish -c "python3 /home/daniel/automation/get_going_script_on_startup.py; exec fish"


import subprocess
import requests

# Global variables
script_paths="/home/daniel/automation/"

print("--------------------------------------------")
print("Hello my dear Daniel, I'm here for you and I'm gonna get you going!")

print("First, what do you want to do today?")
print("0. Nothing")
print("1. Work")
print("2. Study")
print("3. Language")

choice = input("Enter your choice: ")

# check for valid number input
while not choice.isdigit() or int(choice) < 0 or int(choice) > 3:
    choice = input("Enter a valid choice: ")

choice = int(choice)

if (choice == 1):
    print("Let's work!")
    print("I'm gonna open your work applications for you.")
    subprocess.run(['fish', '-c', 'work start'])
elif (choice == 2):
    print("Let's study!")
    print("I'm gonna open your study applications for you.")
    subprocess.run(['fish', '-c', 'study start'])
elif (choice == 3):
    print("Let's learn german!")
    print("I'm gonna open your language learning applications for you.")
    subprocess.run(['fish', '-c', 'lang start'])
else:
    print("All right! I'm gonna let you be wild by your own :)")
    exit()

url = "https://api.quotable.io/random"
response = requests.get(url)
if response.status_code == 200:
    print("--------------------------------------------")
    print("----------------------------------")
    print("------------------------")
    print("--------------")
    print("-----")
    print(response.json()['content'])
    print("- " + response.json()['author'])
    print("-----")
    print("--------------")
    print("------------------------")
    print("----------------------------------")
    print("--------------------------------------------")

print("Have a good day! Love you!")