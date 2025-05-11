import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from src.load_ebird_data import load_ebird_data
from src.clean_and_explore import clean_data
from src.analyze import species_by_location, rare_birds, distance_traveled_analysis

# Load and clean the data
ebird_path = r"/Users/emersonceccarelli/Projects/AMM/Dev/Avian_Migration_Modeling/Data/MyEBirdData.csv"
df = load_ebird_data(ebird_path)
clean_df = clean_data(df)

# Initialize the Dash app
app = dash.Dash(__name__)

# App Layout
state_name_map = {
    "US-AL": "Alabama", "US-AK": "Alaska", "US-AZ": "Arizona", "US-AR": "Arkansas", "US-CA": "California",
    "US-CO": "Colorado", "US-CT": "Connecticut", "US-DE": "Delaware", "US-FL": "Florida", "US-GA": "Georgia",
    "US-HI": "Hawaii", "US-ID": "Idaho", "US-IL": "Illinois", "US-IN": "Indiana", "US-IA": "Iowa",
    "US-KS": "Kansas", "US-KY": "Kentucky", "US-LA": "Louisiana", "US-ME": "Maine", "US-MD": "Maryland",
    "US-MA": "Massachusetts", "US-MI": "Michigan", "US-MN": "Minnesota", "US-MS": "Mississippi", "US-MO": "Missouri",
    "US-MT": "Montana", "US-NE": "Nebraska", "US-NV": "Nevada", "US-NH": "New Hampshire", "US-NJ": "New Jersey",
    "US-NM": "New Mexico", "US-NY": "New York", "US-NC": "North Carolina", "US-ND": "North Dakota",
    "US-OH": "Ohio", "US-OK": "Oklahoma", "US-OR": "Oregon", "US-PA": "Pennsylvania", "US-RI": "Rhode Island",
    "US-SC": "South Carolina", "US-SD": "South Dakota", "US-TN": "Tennessee", "US-TX": "Texas", "US-UT": "Utah",
    "US-VT": "Vermont", "US-VA": "Virginia", "US-WA": "Washington", "US-WV": "West Virginia",
    "US-WI": "Wisconsin", "US-WY": "Wyoming"
}

app.layout = html.Div(children=[
    html.H1("Bird Migration Dashboard"),

    html.Link(rel='stylesheet', href='/assets/styles.css'),

    dcc.Dropdown(
        id='state-dropdown',
        options=[
            {'label': state_name_map.get(code, code), 'value': code}
            for code in sorted(clean_df['State/Province'].dropna().unique())
        ] + [{'label': 'All States', 'value': 'All States'}],
        value='All States',
        placeholder='Select a state',
        style={'backgroundColor': 'white', 'color': 'black', 'cursor': 'pointer'}
    ),

    dcc.Dropdown(
        id='county-dropdown',
        options=[  # Initially all counties will be shown
            {'label': county, 'value': county}
            for county in sorted(clean_df['County'].dropna().unique())
        ],
        placeholder='Select a county',
        style={'backgroundColor': 'white', 'color': 'black', 'cursor': 'pointer'}
    ),

    dcc.Dropdown(
        id='location-dropdown',
        options=[  # Initially all locations will be shown
            {'label': location, 'value': location}
            for location in sorted(clean_df['Location'].dropna().unique())
        ],
        placeholder='Select a location',
        style={'backgroundColor': 'white', 'color': 'black', 'cursor': 'pointer'}
    ),

    dcc.Dropdown(
        id='analysis-dropdown',
        options=[
            {'label': 'Species by Location', 'value': 'species_by_location'}
            ,{'label': 'Rare Birds', 'value': 'rare_birds'}
            # ,{'label': 'Distance Traveled', 'value': 'distance_traveled_analysis'}
        ],
        value='species_by_location',
        style={'backgroundColor': 'white', 'color': 'black', 'cursor': 'pointer'}
    ),

    dcc.Graph(id='analysis-graph')
])

# County dropdown callback
@app.callback(
    Output('county-dropdown', 'options'),
    Input('state-dropdown', 'value')
)
def update_county_dropdown(selected_state):
    if selected_state == 'All States':
        return [{'label': county, 'value': county} for county in sorted(clean_df['County'].dropna().unique())]
    
    counties = clean_df[clean_df['State/Province'] == selected_state]['County'].dropna().unique()
    return [{'label': county, 'value': county} for county in sorted(counties)]

# Location dropdown callback
@app.callback(
    Output('location-dropdown', 'options'),
    [Input('state-dropdown', 'value'),
     Input('county-dropdown', 'value')]
)
def update_location_dropdown(selected_state, selected_county):
    if selected_state == 'All States' or selected_county in [None, 'All Counties']:
        return [{'label': location, 'value': location} for location in sorted(clean_df['Location'].dropna().unique())]
    
    locations = clean_df[
        (clean_df['State/Province'] == selected_state) &
        (clean_df['County'] == selected_county)
    ]['Location'].dropna().unique()

    return [{'label': loc, 'value': loc} for loc in sorted(locations)]

# Graph callback
@app.callback(
    Output('analysis-graph', 'figure'),
    Input('analysis-dropdown', 'value'),
    Input('state-dropdown', 'value'),
    Input('county-dropdown', 'value'),
    Input('location-dropdown', 'value')
)
def update_graph(analysis_type, selected_state, selected_county, selected_location):
    filtered_df = clean_df.copy()

    # Apply filters
    if selected_state != 'All States':
        filtered_df = filtered_df[filtered_df['State/Province'] == selected_state]

    if selected_county not in [None, 'All Counties']:
        filtered_df = filtered_df[filtered_df['County'] == selected_county]

    if selected_location not in [None, 'All Locations']:
        filtered_df = filtered_df[filtered_df['Location'] == selected_location]

    # Run selected analysis
    if analysis_type == 'species_by_location':
        return species_by_location(filtered_df)
    elif analysis_type == 'rare_birds':
        return rare_birds(filtered_df)
    elif analysis_type == 'distance_traveled_analysis':
        return distance_traveled_analysis(filtered_df)

    return {}

if __name__ == '__main__':
    app.run(debug=True)
