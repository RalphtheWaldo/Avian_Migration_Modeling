import pandas as pd
import matplotlib.pyplot as plt
from src.load_ebird_data import load_ebird_data

def clean_data(df):
    """Clean and preprocess eBird data."""
    # Convert 'Count' to numeric (handling errors gracefully)
    df['Count'] = pd.to_numeric(df['Count'], errors='coerce')
    
    # Drop rows with null values in critical columns (e.g., Count, Location, Date)
    df = df.dropna(subset=['Count', 'Location', 'Date'])
    
    # Handle missing 'Duration (Min)' and 'Distance Traveled (km)' by filling with 0
    df.loc[:, 'Duration (Min)'] = df['Duration (Min)'].fillna(0)
    df.loc[:, 'Distance Traveled (km)'] = df['Distance Traveled (km)'].fillna(0)
    
    # Perform any additional cleaning or processing here as needed
    # For example, remove rows with no 'Common Name' (species)
    df = df[df['Common Name'].notna()]
    
    return df

def plot_bird_counts_by_location(df):
    """Plot the number of observations by location."""
    location_counts = df['State/Province'].value_counts()
    location_counts.plot(kind='bar', figsize=(12, 6))
    plt.title('Bird Observations by Location')
    plt.xlabel('Location')
    plt.ylabel('Number of Observations')
    plt.xticks(rotation=90)
    plt.show()

def main():
    file_path = 'data/MyEBirdData.csv'
    df = load_ebird_data(file_path)
    
    if df is not None:
        df = clean_data(df)
        print(df.head())  # Check cleaned data
        
        # Plot observations by location
        plot_bird_counts_by_location(df)

if __name__ == "__main__":
    main()
