import os
import pandas as pd


def load_hr_data(file_name: str | None = None) -> pd.DataFrame:
    """
    Load HR dataset from project_root/data/raw folder.

    - If file_name is given, tries to load that file.
    - If file_name is None, it will automatically pick the first .csv file
      found in data/raw.
    """

    # Folder of this file → src
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Project root = one level above src
    project_root = os.path.dirname(current_dir)

    raw_dir = os.path.join(project_root, "data", "raw")

    if not os.path.exists(raw_dir):
        raise FileNotFoundError(f"'data/raw' folder not found at: {raw_dir}")

    # If no file_name passed, automatically pick first CSV
    if file_name is None:
        csv_files = [f for f in os.listdir(raw_dir) if f.lower().endswith(".csv")]
        if not csv_files:
            raise FileNotFoundError(
                f"No CSV files found in {raw_dir}. "
                f"Please put your HR dataset CSV inside this folder."
            )
        file_name = csv_files[0]  # Pick the first CSV file
        print(f"[INFO] No file_name given. Using: {file_name}")

    file_path = os.path.join(raw_dir, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    print(f"[INFO] Loading dataset from: {file_path}")
    return pd.read_csv(file_path)
