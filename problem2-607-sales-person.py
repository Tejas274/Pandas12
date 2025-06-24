import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(company, on='com_id', how='inner')
    df = df[df['name'] == 'RED']
    df_result = sales_person.merge(df, on='sales_id', how='left')
    df_result = df_result[df_result['com_id'].isna()]
    return df_result[['name_x']].rename(columns={'name_x': 'name'})
