import streamlit as st
import pandas as pd
from export import export_csv

from database import create_tables
from auth import create_admin, login
from employee import (
    add_employee,
    get_all_employees,
    search_employee,
    get_employee_by_id,
    update_employee,
    delete_employee,
    get_total_employees,
    get_average_salary,
    get_highest_salary,
    get_lowest_salary,
    get_department_report
)

# --------------------------------------------------
# Initial Setup
# --------------------------------------------------

st.set_page_config(
    page_title="Employee Management System",
    page_icon="👨‍💼",
    layout="wide"
)

create_tables()
create_admin()

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --------------------------------------------------
# Login Page
# --------------------------------------------------

if not st.session_state.logged_in:

    st.title("👨‍💼 Employee Management System")

    st.subheader("Admin Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if login(username, password):

            st.session_state.logged_in = True

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error("Invalid Username or Password")

# --------------------------------------------------
# Main Application
# --------------------------------------------------

else:

    st.sidebar.title("Employee Management")

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Dashboard",
            "Add Employee",
            "View Employees",
            "Search Employee",
            "Update Employee",
            "Delete Employee",
            "Department Report"
        ]
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()
            # ==========================================
    # Dashboard
    # ==========================================

    if menu == "Dashboard":

        st.title("📊 Dashboard")

        total = get_total_employees()
        avg_salary = get_average_salary()
        highest_salary = get_highest_salary()
        lowest_salary = get_lowest_salary()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("👨‍💼 Total Employees", total)
        col2.metric("💰 Average Salary", f"₹{avg_salary:,.2f}")
        col3.metric("📈 Highest Salary", f"₹{highest_salary:,.2f}")
        col4.metric("📉 Lowest Salary", f"₹{lowest_salary:,.2f}")

        st.markdown("---")

        st.subheader("Employee Records")

        employees = get_all_employees()

        if employees:

            df = pd.DataFrame(
                employees,
                columns=[
                    "ID",
                    "Name",
                    "Age",
                    "Gender",
                    "Email",
                    "Phone",
                    "Department",
                    "Designation",
                    "Salary",
                    "Joining Date"
                ]
            )

            st.dataframe(df, use_container_width=True)

        else:
            st.info("No employees available.")

    # ==========================================
    # Add Employee
    # ==========================================

    elif menu == "Add Employee":

        st.title("➕ Add Employee")

        with st.form("employee_form"):

            col1, col2 = st.columns(2)

            with col1:

                name = st.text_input("Employee Name")

                age = st.number_input(
                    "Age",
                    min_value=18,
                    max_value=65,
                    value=22
                )

                gender = st.selectbox(
                    "Gender",
                    [
                        "Male",
                        "Female",
                        "Other"
                    ]
                )

                email = st.text_input("Email")

                phone = st.text_input("Phone Number")

            with col2:

                department = st.text_input("Department")

                designation = st.text_input("Designation")

                salary = st.number_input(
                    "Salary",
                    min_value=0.0,
                    step=1000.0
                )

                joining_date = st.date_input(
                    "Joining Date"
                )

            submitted = st.form_submit_button(
                "Save Employee"
            )

            if submitted:

                add_employee(
                    name,
                    age,
                    gender,
                    email,
                    phone,
                    department,
                    designation,
                    salary,
                    str(joining_date)
                )

                st.success("✅ Employee Added Successfully!")

                st.balloons()
                    # ==========================================
    # View Employees
    # ==========================================

    elif menu == "View Employees":

        st.title("👨‍💼 Employee List")

        employees = get_all_employees()

        if employees:

            df = pd.DataFrame(
                employees,
                columns=[
                    "ID",
                    "Name",
                    "Age",
                    "Gender",
                    "Email",
                    "Phone",
                    "Department",
                    "Designation",
                    "Salary",
                    "Joining Date"
                ]
            )

            st.dataframe(df, use_container_width=True)

        else:

            st.warning("No employee records found.")

    # ==========================================
    # Search Employee
    # ==========================================
            csv = export_csv(employees)

        st.download_button(
            "📥 Download CSV",
            csv,
            file_name="employees.csv",
            mime="text/csv"
)
    elif menu == "Search Employee":

        st.title("🔍 Search Employee")

        keyword = st.text_input(
            "Search by ID, Name, Department or Designation"
        )

        if keyword:

            result = search_employee(keyword)

            if result:

                df = pd.DataFrame(
                    result,
                    columns=[
                        "ID",
                        "Name",
                        "Age",
                        "Gender",
                        "Email",
                        "Phone",
                        "Department",
                        "Designation",
                        "Salary",
                        "Joining Date"
                    ]
                )

                st.dataframe(df, use_container_width=True)

            else:

                st.error("Employee Not Found")

    # ==========================================
    # Update Employee
    # ==========================================

    elif menu == "Update Employee":

        st.title("✏️ Update Employee")

        emp_id = st.number_input(
            "Enter Employee ID",
            min_value=1,
            step=1
        )

        if st.button("Load Employee"):

            employee = get_employee_by_id(emp_id)

            if employee:

                st.session_state.employee = employee

            else:

                st.error("Employee Not Found")

        if "employee" in st.session_state:

            emp = st.session_state.employee

            with st.form("update_form"):

                name = st.text_input(
                    "Name",
                    emp[1]
                )

                age = st.number_input(
                    "Age",
                    min_value=18,
                    max_value=65,
                    value=int(emp[2])
                )

                gender_options = [
                    "Male",
                    "Female",
                    "Other"
                ]

                gender = st.selectbox(
                    "Gender",
                    gender_options,
                    index=gender_options.index(emp[3])
                )

                email = st.text_input(
                    "Email",
                    emp[4]
                )

                phone = st.text_input(
                    "Phone",
                    emp[5]
                )

                department = st.text_input(
                    "Department",
                    emp[6]
                )

                designation = st.text_input(
                    "Designation",
                    emp[7]
                )

                salary = st.number_input(
                    "Salary",
                    value=float(emp[8])
                )

                joining_date = st.text_input(
                    "Joining Date",
                    emp[9]
                )

                submitted = st.form_submit_button(
                    "Update Employee"
                )

                if submitted:

                    update_employee(
                        emp[0],
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

                    st.success("✅ Employee Updated Successfully!")

                    del st.session_state.employee

    # ==========================================
    # Delete Employee
    # ==========================================

    elif menu == "Delete Employee":

        st.title("🗑️ Delete Employee")

        emp_id = st.number_input(
            "Employee ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Employee"):

            employee = get_employee_by_id(emp_id)

            if employee:

                delete_employee(emp_id)

                st.success("Employee Deleted Successfully!")

            else:

                st.error("Employee Not Found")
            # ==========================================
    # Department Report
    # ==========================================

    elif menu == "Department Report":

        st.title("📊 Department Report")

        report = get_department_report()

        if report:

            df = pd.DataFrame(
                report,
                columns=[
                    "Department",
                    "Employees",
                    "Average Salary",
                    "Highest Salary",
                    "Lowest Salary"
                ]
            )

            st.dataframe(df, use_container_width=True)

            st.markdown("---")

            st.subheader("Department Employee Count")

            chart_df = df.set_index("Department")

            st.bar_chart(chart_df["Employees"])

            st.subheader("Average Salary by Department")

            st.bar_chart(chart_df["Average Salary"])

        else:

            st.info("No employee data available.")