from database import execute_query, fetch_all, fetch_one


# ==============================
# Add Employee
# ==============================
def add_employee(name, age, gender, email, phone,
                 department, designation, salary,
                 joining_date):

    query = """
        INSERT INTO employees
        (
            name,
            age,
            gender,
            email,
            phone,
            department,
            designation,
            salary,
            joining_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    values = (
        name,
        age,
        gender,
        email,
        phone,
        department,
        designation,
        salary,
        joining_date
    )

    execute_query(query, values)


# ==============================
# View All Employees
# ==============================
def get_all_employees():

    query = """
        SELECT *
        FROM employees
        ORDER BY id ASC
    """

    return fetch_all(query)


# ==============================
# Search Employee
# ==============================
def search_employee(keyword):

    query = """
        SELECT *
        FROM employees
        WHERE
            CAST(id AS TEXT) LIKE ?
            OR name LIKE ?
            OR department LIKE ?
            OR designation LIKE ?
    """

    keyword = f"%{keyword}%"

    return fetch_all(
        query,
        (
            keyword,
            keyword,
            keyword,
            keyword
        )
    )


# ==============================
# Get Employee By ID
# ==============================
def get_employee_by_id(emp_id):

    query = """
        SELECT *
        FROM employees
        WHERE id = ?
    """

    return fetch_one(query, (emp_id,))


# ==============================
# Update Employee
# ==============================
def update_employee(
    emp_id,
    name,
    age,
    gender,
    email,
    phone,
    department,
    designation,
    salary,
    joining_date
):

    query = """
        UPDATE employees
        SET
            name=?,
            age=?,
            gender=?,
            email=?,
            phone=?,
            department=?,
            designation=?,
            salary=?,
            joining_date=?
        WHERE id=?
    """

    values = (
        name,
        age,
        gender,
        email,
        phone,
        department,
        designation,
        salary,
        joining_date,
        emp_id
    )

    execute_query(query, values)


# ==============================
# Delete Employee
# ==============================
def delete_employee(emp_id):

    query = """
        DELETE FROM employees
        WHERE id=?
    """

    execute_query(query, (emp_id,))


# ==============================
# Dashboard Analytics
# ==============================
def get_total_employees():

    query = """
        SELECT COUNT(*)
        FROM employees
    """

    result = fetch_one(query)

    return result[0]


def get_average_salary():

    query = """
        SELECT AVG(salary)
        FROM employees
    """

    result = fetch_one(query)

    return result[0] if result[0] else 0


def get_highest_salary():

    query = """
        SELECT MAX(salary)
        FROM employees
    """

    result = fetch_one(query)

    return result[0] if result[0] else 0


def get_lowest_salary():

    query = """
        SELECT MIN(salary)
        FROM employees
    """

    result = fetch_one(query)

    return result[0] if result[0] else 0


# ==============================
# Department Report
# ==============================
def get_department_report():

    query = """
        SELECT
            department,
            COUNT(*),
            AVG(salary),
            MAX(salary),
            MIN(salary)
        FROM employees
        GROUP BY department
    """

    return fetch_all(query)