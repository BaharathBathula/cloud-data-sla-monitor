import pandas as pd

def check_nulls(df: pd.DataFrame, column: str, max_null_pct: float = 0.0):
    """
    Returns:
      (pass_bool, null_pct_float)
    """
    null_pct = df[column].isnull().mean()
    return null_pct <= max_null_pct, float(null_pct)

def check_row_count(df: pd.DataFrame, min_rows: int):
    """
    Returns:
      (pass_bool, row_count_int)
    """
    row_count = len(df)
    return row_count >= min_rows, int(row_count)

