import pandas as pd
import os

def load_ebird_data(filepath):
    """
    Load eBird CSV data into a pandas DataFrame.

    Parameters:
    filepath (str): Path to the eBird CSV file.

    Returns:
    pd.DataFrame: Loaded eBird data.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No file found at: {filepath}")
    
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df):,} records from {filepath}")
    return df

def explore_ebird_data(df):
    """
    Perform basic exploration of the eBird data.
    """
    print("\n--- Dataset Info ---")
    print(df.info())

    print("\n--- First 5 Rows ---")
    print(df.head())

    print("\n--- Summary Stats ---")
    print(df.describe(include='all'))

def main():
    ebird_path = r"/Users/emersonceccarelli/Projects/AMM/Dev/Avian_Migration_Modeling/Data/MyEBirdData.csv"  # Adjust path as needed
    try:
        df_ebird = load_ebird_data(ebird_path)
        explore_ebird_data(df_ebird)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
