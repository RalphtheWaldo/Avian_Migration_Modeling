from dash import dash

eBird_Dashboard = dash(__name__)

eBird_Dashboard.css.append_css({
    'external_url': '/assets/styles.css'
})