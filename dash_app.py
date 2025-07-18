import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load your cleaned sales data from Task 2
df = pd.read_csv('your_sales_data.csv')  # 🔁 Replace with actual filename
df['date'] = pd.to_datetime(df['date'])
df.sort_values('date', inplace=True)

# Create the line chart
fig = px.line(df, x='date', y='sales',
              title='Sales Over Time',
              labels={'date': 'Date', 'sales': 'Total Sales'},
              markers=True)

# Add vertical line for the price increase on Jan 15, 2021
fig.add_vline(x='2021-01-15', line_dash='dash', line_color='red',
              annotation_text="Price Increase", annotation_position="top left")

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Soul Foods Sales Visualiser", style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    ),

    html.P("Red dashed line = Pink Morsel price increase (15 Jan 2021)", 
           style={'textAlign': 'center'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
