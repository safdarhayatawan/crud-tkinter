Lecture : Opening a file.
file = open('data.txt','r')


Lecture : Reading data from a file.
file = open('data.txt','r')
content  = file.read()
print(content)


content  = file.read(10)


content  = file.readline()


file = open('data.txt','r')
content  = file.readline()
print(content)
file.close()


Lecture : Writing data to a file


file = open('data.txt','w')
file.write('New content to be added to file')
file.close()


Lecture : Appending data to a file.
file = open('data.txt','a')
content  = 'New content to be added to file'
file.write(content)
file.close()
content  = '\\nNew content to be added to file'


Lecture: Opening a file using with
# Open a file using "with" statement
with open("example.txt", "r") as file:
    # Read and print the contents of the file
    contents = file.read()
    print(contents)


Lecture: Readline and readlines


Create a file with the following content

hello
world
Now write this code to read line:

with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
 
print("Line 1:", line1)
print("Line 2:", line2)
Readlines


with open("example.txt", "r") as file:
    lines = file.readlines()
 
print("Lines:", lines)
Now access evvery single line from the list by looping through the list:

for line in lines:
    print(line)


Lecture: Strip, lstrip and rstrip
.

Here is an example of the strip method:

text = "   Hello, World!   "
stripped_text = text.strip()
 
print(stripped_text)  # Output: "Hello, World!"
The lstrip() method:

text = "   Hello, World!   "
left_stripped_text = text.lstrip()
 
print(left_stripped_text)  # Output: "Hello, World!   "
The rstrip() method:

text = "   Hello, World!   "
right_stripped_text = text.rstrip()
 
print(right_stripped_text)  # Output: "   Hello, World!"
Using strip to remove whitespaces from the previous program.

with open("names.txt", "r") as file:
    lines = file.readlines()
 
for line in lines:
    print(line.strip())
Lecture: Save data into a file
file = open("names.txt", "a")
 
while True:
    name = input('Enter name to be added: ')
    file.write(name+'\\n')
    choice = input("Do you want to add more names? (y/n)")
    if choice == 'n':
	file.close()
        break


Lecture: Reading data from the file.
Write a program to get all the entered names and then capitalize them

file = open("names.txt", "a")
 
while True:
    name = input('Enter name to be added: ')
    file.write(name+'\\n')
    choice = input("Do you want to add more names? (y/n)")
    if choice == 'n':
        file.close()
        break
 
# write code to read all the names in the file and capitalize them.
file = open("names.txt", "r")
lines = file.readlines()
 
for line in lines:
    print(line.strip().capitalize())
    # capitalize every line
Lecture : Saving complex data into a file
def save_user_data():
    # Accept user input for name, email, and contact
    name = input("Enter name: ")
    email = input("Enter email: ")
    contact = input("Enter contact: ")
 
    # Create a string with the user data
    user_data = f"Name: {name}\\nEmail: {email}\\nContact: {contact}\\n"
 
    # Open the file in append mode and write the user data
    #if you use with, you don't have to close the file back.
    with open("user_data.txt", "a") as file:
        file.write(user_data)
 
    print("User data saved successfully!")
 
def read_user_data():
    # Open the file in read mode
    with open("user_data.txt", "r") as file:
        # Read and print the file contents
        print(file.read())
 
# Save user data
save_user_data()
 
# Read user data from file
read_user_data()


Lecture : Serialising data using JSON
Create a simple Python dictionary.

import json
 
# Create a Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
 
# Serialize the data to a JSON string
json_data = json.dumps(data)
#The json.dumps() function is used to convert the data dictionary into 
#a JSON string.
 
print(json_data)
json.loads()  example:

import json
 
# JSON string
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'
 
# Deserialize the JSON string to a Python dictionary
data = json.loads(json_data)
 
print(data)
print(data["name"])
print(data["age"])
print(data["city"])


Lecture: Storing JSON data in a file.


import json
import os
 
def save_user_data():
    user_list = []
 
    while True:
        # Accept user input for name, email, and contact
        name = input("Enter name (or 'quit' to exit): ")
 
        if name.lower() == "quit":
            break
 
        email = input("Enter email: ")
        contact = input("Enter contact: ")
 
        # Create a dictionary with the user data
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
 
        user_list.append(user_data)
 
    if os.path.exists("user_data.json"):
        # Load existing user data from the file
        with open("user_data.json", "r") as file:
            existing_data = json.load(file)
 
        # Append the new user data to the existing data
        user_list.extend(existing_data)
 
    # Open the file in write mode and save the user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
 
    print("User data saved successfully!")
 
def read_user_data():
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return
 
    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)
 
    # Print the user data
    print("User Data:")
    for user_data in user_list:
        print("Name:", user_data["name"])
        print("Email:", user_data["email"])
        print("Contact:", user_data["contact"])
        print()
 
# Save user data
save_user_data()
 
# Read user data from file
read_user_data()


Lecture: Editing data functionality


import json
import os
 
def save_user_data():
    user_list = []
 
    while True:
        # Accept user input for name, email, and contact
        name = input("Enter name (or 'quit' to exit): ")
 
        if name.lower() == "quit":
            break
 
        email = input("Enter email: ")
        contact = input("Enter contact: ")
 
        # Create a dictionary with the user data
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
 
        user_list.append(user_data)
 
    if os.path.exists("user_data.json"):
        # Load existing user data from the file
        with open("user_data.json", "r") as file:
            existing_data = json.load(file)
 
        # Append the new user data to the existing data
        user_list.extend(existing_data)
 
    # Open the file in write mode and save the user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
 
    print("User data saved successfully!")
 
def read_user_data():
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return
 
    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)
 
    # Print the user data
    print("User Data:")
    for user_data in user_list:
        print("Name:", user_data["name"])
        print("Email:", user_data["email"])
        print("Contact:", user_data["contact"])
        print()
 
def edit_user_data(name):
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return
 
    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)
 
    user_found = False
 
    # Search for the user based on the name
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            # Prompt the user for updated email and contact
            email = input("Enter updated email: ")
            contact = input("Enter updated contact: ")
 
            # Update the user data
            user_data["email"] = email
            user_data["contact"] = contact
 
            user_found = True
            break
 
    if not user_found:
        print("User not found.")
 
    # Open the file in write mode and save the updated user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
 
    print("User data updated successfully!")
 
# Save user data
save_user_data()
 
# Read user data from file
read_user_data()
 
# Edit user data
edit_name = input('Enter name which you want to edit')
edit_user_data(edit_name)  # Pass the name of the user you want to edit
 
# Read user data again to verify the changes
read_user_data()


Lecture: Delete functionality
import json
import os
 
def save_user_data():
    user_list = []
 
    while True:
        # Accept user input for name, email, and contact
        name = input("Enter name (or 'quit' to exit): ")
 
        if name.lower() == "quit":
            break
 
        email = input("Enter email: ")
        contact = input("Enter contact: ")
 
        # Create a dictionary with the user data
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
 
        user_list.append(user_data)
 
    if os.path.exists("user_data.json"):
        # Load existing user data from the file
        with open("user_data.json", "r") as file:
            existing_data = json.load(file)
 
        # Append the new user data to the existing data
        user_list.extend(existing_data)
 
    # Open the file in write mode and save the user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
 
    print("User data saved successfully!")
 
def read_user_data():
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return
 
    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)
 
    # Print the user data
    print("User Data:")
    for user_data in user_list:
        print("Name:", user_data["name"])
        print("Email:", user_data["email"])
        print("Contact:", user_data["contact"])
        print()
 
def edit_user_data(name):
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return
 
    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)
 
    user_found = False
 
    # Search for the user based on the name
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            # Prompt the user for updated email and contact
            email = input("Enter updated email: ")
            contact = input("Enter updated contact: ")
 
            # Update the user data
            user_data["email"] = email
            user_data["contact"] = contact
 
            user_found = True
            break
 
    if not user_found:
        print("User not found.")
 
    # Open the file in write mode and save the updated user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
 
    print("User data updated successfully!")
 
def delete_user_data(name):
    # Check if the file exists
    if not os.path.exists("user_data.json"):
        print("No user data found.")
        return
 
    # Open the file in read mode
    with open("user_data.json", "r") as file:
        # Load the JSON data
        user_list = json.load(file)
 
    user_found = False
 
    # Search for the user based on the name
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            # Remove the user data from the list
            user_list.remove(user_data)
 
            user_found = True
            break
 
    if not user_found:
        print("User not found.")
 
    # Open the file in write mode and save the updated user data as JSON
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
 
    print("User data deleted successfully!")
 
# Save user data
save_user_data()
 
# Read user data from file
read_user_data()
 
# Edit user data
edit_name = input('Enter name which you want to edit')
edit_user_data(edit_name)  # Pass the name of the user you want to edit
 
# Read user data again to verify the changes
read_user_data()
 
# Delete user
delete_user = input('Enter the name of user you want to delete')
delete_user_data(delete_user)




