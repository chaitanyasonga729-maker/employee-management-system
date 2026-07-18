import pandas as pd
from employee import add_employee, get_all_employees

if st.button("Login"):
    if login(username, password):

        st.success("Login Successful")

        menu = st.sidebar.selectbox(
            "Menu",
            ["Dashboard", "Add Employee", "View Employees"]
        )

        if menu == "Dashboard":

            st.title("Dashboard")

            employees = get_all_employees()

            st.metric("Total Employees", len(employees))

        elif menu == "Add Employee":

            st.title("Add Employee")

            name = st.text_input("Name")
            age = st.number_input("Age", 18, 65)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            department = st.text_input("Department")
            designation = st.text_input("Designation")
            salary = st.number_input("Salary", 0)
            joining_date = st.date_input("Joining Date")

            if st.button("Save Employee"):

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

                st.success("Employee Added Successfully!")

        elif menu == "View Employees":

            st.title("Employee List")

            data = get_all_employees()

            df = pd.DataFrame(
                data,
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

            st.dataframe(df)

    else:
        st.error("Invalid Username or Password")