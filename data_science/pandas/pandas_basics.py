#A DataFrame is a Pandas structure that stores data in rows and columns, similar to an Excel table.

#It makes it easy to view, filter, modify, and analyze structured data.

# It makes it easy to view, filter, modify, and analyze structured data.

import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit"],
    "Salary": [60000, 55000, 70000],
    "Department": ["IT", "HR", "IT"]
}

df = pd.DataFrame(data)

print(df)