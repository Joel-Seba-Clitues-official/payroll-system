from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary REAL NOT NULL
                )''')
    conn.commit()
    conn.close()

# Home Page - List Employees
@app.route('/')
def index():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('SELECT * FROM employees')
    employees = c.fetchall()
    conn.close()
    return render_template('index.html', employees=employees)

# Add Employee - Form
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']

        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute('INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)', 
                  (name, position, salary))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_employee.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000) # Change port as needed
