import pandas as pd

def export_csv(data):
    columns = [
        "ID","Name","Age","Gender","Email","Phone",
        "Department","Designation","Salary","Joining Date"
    ]

    df = pd.DataFrame(data, columns=columns)

    return df.to_csv(index=False).encode("utf-8")