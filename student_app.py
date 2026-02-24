from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# ===== CONNECTION =====
client = MongoClient("mongodb+srv://shailesh:Shailesh123@cluster0.fkkg9xb.mongodb.net/?appName=Cluster0")

db = client["school"]
collection = db["students"]

# Make roll unique
collection.create_index("roll", unique=True)


# ===== FUNCTIONS =====

def add_student():
    try:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        collection.insert_one(student)
        print("✅ Student Added Successfully!\n")

    except DuplicateKeyError:
        print("❌ Roll Number already exists!\n")

    except Exception as e:
        print("Error:", e)


def view_students():
    students = collection.find()
    print("\n📋 Student Records:")
    for student in students:
        print(f"Roll: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}")
    print()


def update_marks():
    roll = int(input("Enter Roll No to Update: "))
    new_marks = float(input("Enter New Marks: "))

    result = collection.update_one(
        {"roll": roll},
        {"$set": {"marks": new_marks}}
    )

    if result.modified_count > 0:
        print("✅ Marks Updated Successfully!\n")
    else:
        print("❌ Student Not Found!\n")


def delete_student():
    roll = int(input("Enter Roll No to Delete: "))

    result = collection.delete_one({"roll": roll})

    if result.deleted_count > 0:
        print("✅ Student Deleted Successfully!\n")
    else:
        print("❌ Student Not Found!\n")


# ===== MENU =====

while True:
    print("====== Student Management System (MongoDB Atlas) ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!\n")