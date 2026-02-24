from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# ===== MongoDB Connection =====
client = MongoClient("mongodb+srv://shailesh:Shailesh123@cluster0.fkkg9xb.mongodb.net/?appName=Cluster0")
db = client["school"]
collection = db["students"]
collection.create_index("roll", unique=True)

# ===== Window Setup =====
root = Tk()
root.title("Student Management System")
root.geometry("600x550")
root.config(bg="#e6f2ff")

# ===== Functions =====

def clear_fields():
    roll_entry.delete(0, END)
    name_entry.delete(0, END)
    marks_entry.delete(0, END)

def add_student():
    try:
        roll = int(roll_entry.get())
        name = name_entry.get()
        marks = int(marks_entry.get())

        collection.insert_one({"roll": roll, "name": name, "marks": marks})
        messagebox.showinfo("Success", "Student Added Successfully!")
        clear_fields()
    except DuplicateKeyError:
        messagebox.showerror("Error", "Roll Number Already Exists!")
    except:
        messagebox.showerror("Error", "Please Enter Valid Data!")

def view_students():
    text_area.delete("1.0", END)
    students = collection.find()

    for student in students:
        text_area.insert(END, f"Roll: {student['roll']}  |  "
                              f"Name: {student['name']}  |  "
                              f"Marks: {student['marks']}\n")

def update_student():
    try:
        roll = int(roll_entry.get())
        marks = int(marks_entry.get())

        result = collection.update_one(
            {"roll": roll},
            {"$set": {"marks": marks}}
        )

        if result.modified_count > 0:
            messagebox.showinfo("Success", "Marks Updated Successfully!")
        else:
            messagebox.showerror("Error", "Student Not Found!")
        clear_fields()
    except:
        messagebox.showerror("Error", "Please Enter Valid Data!")

def delete_student():
    try:
        roll = int(roll_entry.get())

        result = collection.delete_one({"roll": roll})

        if result.deleted_count > 0:
            messagebox.showinfo("Success", "Student Deleted Successfully!")
        else:
            messagebox.showerror("Error", "Student Not Found!")
        clear_fields()
    except:
        messagebox.showerror("Error", "Please Enter Valid Data!")

# ===== UI Design =====

Label(root, text="Student Management System",
      font=("Arial", 22, "bold"),
      bg="#e6f2ff", fg="#003366").pack(pady=20)

form_frame = Frame(root, bg="#e6f2ff")
form_frame.pack()

Label(form_frame, text="Roll No:", font=("Arial", 12),
      bg="#e6f2ff").grid(row=0, column=0, pady=10, padx=10)

roll_entry = Entry(form_frame, font=("Arial", 12))
roll_entry.grid(row=0, column=1, pady=10)

Label(form_frame, text="Name:", font=("Arial", 12),
      bg="#e6f2ff").grid(row=1, column=0, pady=10)

name_entry = Entry(form_frame, font=("Arial", 12))
name_entry.grid(row=1, column=1, pady=10)

Label(form_frame, text="Marks:", font=("Arial", 12),
      bg="#e6f2ff").grid(row=2, column=0, pady=10)

marks_entry = Entry(form_frame, font=("Arial", 12))
marks_entry.grid(row=2, column=1, pady=10)

# Buttons Section
btn_frame = Frame(root, bg="#e6f2ff")
btn_frame.pack(pady=20)

Button(btn_frame, text="Add Student", width=15,
       bg="#4CAF50", fg="white",
       command=add_student).grid(row=0, column=0, padx=10)

Button(btn_frame, text="View Students", width=15,
       bg="#2196F3", fg="white",
       command=view_students).grid(row=0, column=1, padx=10)

Button(btn_frame, text="Update Marks", width=15,
       bg="#FFC107",
       command=update_student).grid(row=1, column=0, pady=10)

Button(btn_frame, text="Delete Student", width=15,
       bg="#F44336", fg="white",
       command=delete_student).grid(row=1, column=1, pady=10)

# Text Area
text_area = Text(root, height=8, width=70, font=("Arial", 11))
text_area.pack(pady=20)

root.mainloop()