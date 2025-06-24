import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    df_magaer_id = employee.groupby("managerId").count().reset_index()[["managerId","department"]]
    df_filtered_magaer_ids = df_magaer_id[df_magaer_id["department"]>=5]
    manager_ids_to_filter = df_filtered_magaer_ids['managerId'].unique()
    return employee[employee['id'].isin(manager_ids_to_filter)][['name']]