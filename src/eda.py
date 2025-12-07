import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_attrition_by_department(df: pd.DataFrame,
                                 department_col: str = "Department",
                                 attrition_col: str = "Attrition"):
    sns.countplot(data=df, x=department_col, hue=attrition_col)
    plt.title("Attrition by Department")
    plt.xticks(rotation=45)
    plt.tight_layout()


def correlation_heatmap(df: pd.DataFrame, numeric_cols=None):
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=False)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
