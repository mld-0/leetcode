import pandas as pd

#   DataFrame.drop_duplicates(subset=None, *, keep='first', inplace=False, ignore_index=False)
#
#   subset: column label(s) to filter for duplicates
#   keep: 'first' keep first duplicate, 'last' keep last duplicate, False drop all duplicates
#   inplace: whether to modify existing df or create new one
#   ignore_index: if True, resulting rows will be re-labeled 0,1,...,n-1

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers


data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}

df = pd.DataFrame(data)
print(f"df=({df})")
dropDuplicateEmails(df)
print(f"result=({df})")

