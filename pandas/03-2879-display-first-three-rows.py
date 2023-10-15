import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    print(employees.loc[:2])
    print()
    #   or
    print(employees[:3])
    print()
    #   or
    print(employees.head(3))
    print()


data = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

df = pd.DataFrame(data)
print(f"df=({df})")
selectFirstRows(df)

