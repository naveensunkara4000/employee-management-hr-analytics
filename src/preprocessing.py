import pandas as pd

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Example basic cleaning:
    - Drop duplicate rows
    - Handle missing values (simple strategy)
    """
    df = df.drop_duplicates()

    # Simple missing value handling
    for col in df.columns:
        if df[col].dtype == "O":  # object / string
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(df[col].median())

    return df
