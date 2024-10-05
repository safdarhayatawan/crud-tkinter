import psycopg2

def create_table():
    conn = psycopg2.connect(dbname='studentdb',user='postgres', password='safdar@111',host='localhost',port='5432')
    cur = conn.cursor()
    cur.execute('create table student2(student_id serial primary key,name text, address text,age int,number text);')
    print('student2 table is created')
    conn.commit()
    conn.close()


def insert_data():
    # code to accept data from the user
    name = input("enter the name: ")
    address = input("enter the address: ")
    age = input("enter the age: ")
    number = input("enter the number: ")

    conn = psycopg2.connect(dbname='studentdb',user='postgres', password='safdar@111',host='localhost',port='5432')
    cur = conn.cursor()
    cur.execute("insert into student2(name,address,age,number) values (%s,%s,%s,%s)",(name,address,age,number))
    print('student2 table has one more entry')
    conn.commit()
    conn.close()

def update_data():
    student_id = input("Enter ID of the student to be updated: ")
    
    # Database connection setup
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='safdar@111', host='localhost', port='5432')
    cur = conn.cursor()
    
    # Fields dictionary containing the possible fields to update
    fields = {
        "1": ("name", "Enter the new name: "),
        "2": ("address", "Enter the new address: "),
        "3": ("age", "Enter the new age: "),
        "4": ("number", "Enter the new number: ")
    }
    
    # Display the fields available for update
    print("Which field would you like to update?")
    for key in fields:
        print(f"{key}: {fields[key][0]}")  # Show the field number and the field name
    
    # Get the user's choice
    field_choice = input("Enter the number of the field you want to update: ")
    
    # Check if the choice is valid
    if field_choice in fields:
        # Get the field name and the prompt
        field_info = fields[field_choice]  # field_info is a tuple like ("name", "enter the new name")
        field_name = field_info[0]         # Field name (e.g., "name")
        prompt = field_info[1]             # Prompt message (e.g., "Enter the new name: ")

        # Ask the user to input the new value
        new_value = input(prompt)

        # SQL query to update the database
        sql = f"UPDATE student2 SET {field_name} = %s WHERE student_id = %s"
        cur.execute(sql, (new_value, student_id))
        
        print(f"{field_name.capitalize()} updated successfully!")
    else:
        print("Invalid choice.")
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# update_data()
def delete_data():
    student_id = input("Enter ID of the student to be deleted: ")  
    # Database connection setup
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='safdar@111', host='localhost', port='5432')
    cur = conn.cursor()

    cur.execute("select * from student2 where student_id=%s",(student_id,))
    student = cur.fetchone()
    if student:
        print(f"Student to be deleted: ID {student[0]}, Name:{student[1]}")
        choice = input("Are you sure to delete the student? (yes/no) ")
        if choice.lower() =="yes":
            cur.execute("delete from student2 where student_id=%s",(student_id,))   
            print("student record is deleted")
        else:
            print("deletion cancel")
    else:
        print("Student not found")
    conn.commit()
    conn.close()
# delete_data()
def read_data():
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='safdar@111', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("select * from student2;")
    students = cur.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address:{student[2]}, Age:{student[3]}") 
    conn.close()        


while True:
    print("\n Welcome to the Student Database Management System")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        create_table()
    elif choice == "2":
        insert_data()
    elif choice =="3":
        read_data()
    elif choice == "4":
        update_data()
    elif choice == "5":
        delete_data()
    elif choice == "6":
        break
    else:
        print("invalid choice")
