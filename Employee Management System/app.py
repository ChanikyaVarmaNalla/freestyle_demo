from functools import wraps

from flask import Flask, render_template, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "kingsman"

# Configure the SQLite database for users
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# for user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# for employee table
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    skills = db.Column(db.JSON, nullable=False)
    qualifications = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return '<Employee %r>' % self.first_name


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '')
        password = request.form.get('password', '')

        # Check if the user exists in the database
        user = User.query.filter_by(username=email).first()

        if user:
            # Check if the password is correct
            if user.password == password:
                # Store the logged-in user's ID in the session
                session['user_id'] = user.id
                flash("Login successful! Welcome to Employee Data.", "success")
                return redirect('/employee_data')  # Redirect to employee_data page
            else:
                flash("Invalid username or password. Please try again.", "error")

        flash("Invalid username or password. Please try again.", "error")
        return render_template("login.html", invalid_credentials=True)

    return render_template("login.html", invalid_credentials=False)

# Create a login_required decorator function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access employee data.", "error")
            return redirect('/login')
        return f(*args, **kwargs)

    return decorated_function

@app.route('/employee_data')
@login_required
def employee_data():
    # Fetch all employee records from the database
    employees = Employee.query.all()

    return render_template("employee_data.html", employees=employees)

@app.route('/employee_data/select', methods=['GET', 'POST'])
@login_required
def select_employee():
    if request.method == 'POST':
        search_query = request.form.get('search_query', '')
        if search_query == '*':
            # Fetch all employee records from the database
            employees = Employee.query.all()
        else:
            # Fetch employees based on the search_query (first name, last name, or both)
            employees = Employee.query.filter(
                (Employee.first_name.contains(search_query)) |
                (Employee.last_name.contains(search_query))
            ).all()

        return render_template("employee_data.html", employees=employees)

    return render_template("select_employee.html")

@app.route('/employee_data/insert', methods=['GET', 'POST'])
@login_required
def insert_employee():
    if request.method == 'POST':
        # Get the employee details from the form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = int(request.form['age'])
        experience = int(request.form['experience'])
        salary = float(request.form['salary'])
        skills = request.form['skills'].split(', ')
        qualifications = request.form['qualifications'].split(', ')

        # Create a new employee instance
        new_employee = Employee(
            first_name=first_name,
            last_name=last_name,
            age=age,
            experience=experience,
            salary=salary,
            skills=skills,
            qualifications=qualifications
        )

        # Add the new employee to the database
        db.session.add(new_employee)
        db.session.commit()

        # Flash the success message and redirect to the employee_data page
        flash("Employee details added successfully.", "success")
        return redirect('/employee_data')

    return render_template("insert_employee.html")

@app.route('/employee_data/update', methods=['GET', 'POST'])
@login_required
def update_employee():
    if request.method == 'POST':
        # Get the employee name from the form
        employee_name = request.form.get('employee_name', '')

        # Find the employee by their full name
        employee = Employee.query.filter(
            (Employee.first_name + ' ' + Employee.last_name).ilike(f'%{employee_name}%')
        ).first()

        if employee:
            # Fetch the old details of the employee
            old_employee_details = {
                'id': employee.id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'age': employee.age,
                'experience': employee.experience,
                'salary': employee.salary,
                'skills': employee.skills,
                'qualifications': employee.qualifications
            }

            # Render the update_employee.html template with the old details
            return render_template("update_employee.html", employee=old_employee_details)
        else:
            flash("Employee not found. Please try again.", "error")
            return redirect('/employee_data/update')

    return render_template("update_employee.html", employee=None)

@app.route('/employee_data/update_employee/<int:employee_id>', methods=['POST'])
@login_required
def update_employee_details(employee_id):
    if request.method == 'POST':
        # Find the employee by their ID
        employee = Employee.query.get(employee_id)

        if employee:
            # Update the employee details with the new information
            employee.first_name = request.form['first_name']
            employee.last_name = request.form['last_name']
            employee.age = int(request.form['age'])
            employee.experience = int(request.form['experience'])
            employee.salary = float(request.form['salary'])
            employee.skills = request.form['skills'].split(',')
            employee.qualifications = request.form['qualifications'].split(',')

            # Save the changes to the database
            db.session.commit()

            # Flash the success message and redirect to the employee_data page
            flash("Employee details updated successfully.", "success")
            return redirect('/employee_data')

    flash("Employee not found. Please try again.", "error")
    return redirect('/employee_data/update')

@app.route('/employee_data/delete', methods=['GET', 'POST'])
@login_required
def delete_employee():
    if request.method == 'POST':
        # Get the employee name from the form
        employee_name = request.form.get('employee_name', '')

        # Find all employees whose first or last name contains the provided name
        employees = Employee.query.filter(
            (Employee.first_name + ' ' + Employee.last_name).ilike(f'%{employee_name}%')
        ).all()

        if not employees:
            flash("Employee not found. Please try again.", "error")
            return redirect('/employee_data/delete')

        deleted_count = len(employees)

        if deleted_count == 1:
            # If there is only one occurrence, delete that employee
            db.session.delete(employees[0])
        else:
            # If there are multiple occurrences, keep the one with the lowest index and delete the rest
            employees.sort(key=lambda emp: (emp.first_name, emp.last_name))
            keep_employee = employees[0]
            delete_employees = employees[1:]

            for emp in delete_employees:
                db.session.delete(emp)

        db.session.commit()

        if deleted_count > 1:
            flash(f"{deleted_count} duplicate employee(s) deleted successfully.", "success")
        else:
            flash("Employee deleted successfully.", "success")
        return redirect('/employee_data')

    return render_template("delete_employee.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form.get('firstname', '')
        lastname = request.form.get('lastname', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not password or not confirm_password or password != confirm_password:
            flash("Passwords do not match. Please try again.", "error")
            return render_template("signup.html", step=1, signup_status="failed", email=email)

        # Check if the username (email) already exists in the database
        if User.query.filter_by(username=email).first():
            flash("Username (email) already exists. Please choose a different one.", "error")
            return render_template("signup.html", step=1, signup_status="failed", email=email)

        # Create a new user instance and save it to the database
        new_user = User(username=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Pass the new user's credentials to the login.html template for display
        new_user_credentials = {'email': email, 'password': password}

        # Redirect to login page after successful signup and display success message and credentials on login page
        flash("Signup successful! Please log in.", "success")
        return render_template("login.html", new_user=new_user_credentials)

    return render_template("signup.html", step=1, signup_status="not_attempted")

@app.route('/logout')
def logout():
    # Clear the 'user_id' from the session to log the user out
    session.pop('user_id', None)
    flash("You have been logged out.", "success")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
