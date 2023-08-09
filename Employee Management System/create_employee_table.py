# create_employee_table.py

import json
from app import app, db, Employee

def create_employee_table():
    with app.app_context():
        with open("employee_data.json") as f:
            data = json.load(f)
            employees_data = data["employees"]

        # Create the "employee" table and insert data
        db.create_all()
        for employee_data in employees_data:
            employee = Employee(
                id=employee_data["id"],
                first_name=employee_data["first_name"],
                last_name=employee_data["last_name"],
                age=employee_data["age"],
                experience=employee_data["experience"],
                salary=employee_data["salary"],
                skills=json.dumps(employee_data["skills"]),
                qualifications=json.dumps(employee_data["qualifications"])
            )
            db.session.add(employee)

        db.session.commit()

if __name__ == "__main__":
    create_employee_table()
