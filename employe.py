from database import create_connection

def add_employee(name, age, gender, email, phone, department, designation, salary, joining_date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO employees
        (name, age, gender, email, phone, department, designation, salary, joining_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        age,
        gender,
        email,
        phone,
        department,
        designation,
        salary,
        joining_date
    ))

    conn.commit()
    conn.close()


def get_all_employees():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    data = cursor.fetchall()

    conn.close()

    return data