import pandas as pd
import plotly.express as px
from src.load_ebird_data import load_ebird_data
from src.clean_and_explore import clean_data

# def species_by_location(data):
#     location_species_count = (
#         data.groupby(['Location', 'Common Name'])
#         .size()
#         .reset_index(name='Count')
#         .sort_values(by='Count', ascending=False)
#     )

#     top_10_species = location_species_count.head(10)

#     fig = px.bar(
#         top_10_species,
#         x='Count',
#         y='Common Name',
#         color='Location',
#         orientation='h',
#         title='Top 10 Species by Location'
#     )
#     fig.update_layout(yaxis={'categoryorder': 'total ascending'})
#     return fig

def species_by_location(data):
    # Group by species and location, count sightings
    species_location_count = data.groupby(['Common Name', 'Location']).size().reset_index(name='Count')

    # Get top 10 species overall (regardless of location)
    top_species = species_location_count.groupby('Common Name')['Count'].sum().nlargest(10).index

    # Filter to just those species
    filtered = species_location_count[species_location_count['Common Name'].isin(top_species)]

    # Plot: one bar per species, stacked by location
    fig = px.bar(
        filtered,
        x='Common Name',
        y='Count',
        color='Location',
        title='Top 10 Bird Species by Location (Stacked)',
        barmode='stack'
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig



def rare_birds(data, threshold=5):
    species_count = (
        data.groupby('Common Name')
        .size()
        .reset_index(name='Count')
    )
    
    rare_species = species_count[species_count['Count'] < threshold].sort_values(by='Count')

    fig = px.bar(
        rare_species,
        x='Common Name',
        y='Count',
        title=f'Rare Birds (Less than {threshold} Observations)'
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig

def distance_traveled_analysis(data):
    distance_data = data[data['Distance Traveled (km)'].notnull()]
    species_distance = (
        distance_data.groupby('Common Name')['Distance Traveled (km)']
        .sum()
        .reset_index()
        .sort_values(by='Distance Traveled (km)', ascending=False)
    )

    top_10_distance = species_distance.head(10)

    fig = px.bar(
        top_10_distance,
        x='Distance Traveled (km)',
        y='Common Name',
        orientation='h',
        title='Top 10 Species by Total Distance Traveled'
    )
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    return fig

# Optional: for standalone exploration
def main():
    ebird_path = r"/Users/emersonceccarelli/Projects/AMM/Dev/Avian_Migration_Modeling/Data/MyEBirdData.csv"
    df_ebird = load_ebird_data(ebird_path)
    clean_df = clean_data(df_ebird)

    # Uncomment one to preview
    species_by_location(clean_df).show()
    # rare_birds(clean_df).show()
    # distance_traveled_analysis(clean_df).show()
