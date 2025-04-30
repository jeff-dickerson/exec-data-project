#!/usr/bin/env python3
"""
plot_crude_trend.py

Creates an interactive dashboard for crude oil production trends
using Plotly.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

def load_data():
    """Load and prepare the crude oil production data."""
    df = pd.read_csv('../data/raw/crude_production_24mo.csv')
    df['period'] = pd.to_datetime(df['period'])
    return df

def create_dashboard(df):
    """Create an interactive dashboard with multiple plots."""
    # Create figure with secondary y-axis
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Crude Oil Production Trend', 'Month-over-Month Change'),
        vertical_spacing=0.15
    )

    # Add production line
    fig.add_trace(
        go.Scatter(
            x=df['period'],
            y=df['production'],
            name='Production',
            line=dict(color='blue')
        ),
        row=1, col=1
    )

    # Calculate and add month-over-month change
    df['mom_change'] = df['production'].pct_change() * 100
    fig.add_trace(
        go.Bar(
            x=df['period'],
            y=df['mom_change'],
            name='MoM Change',
            marker_color='green'
        ),
        row=2, col=1
    )

    # Update layout
    fig.update_layout(
        title_text='U.S. Crude Oil Production Dashboard',
        height=800,
        showlegend=True
    )

    # Update y-axes labels
    fig.update_yaxes(title_text='Production (k bbl/day)', row=1, col=1)
    fig.update_yaxes(title_text='Month-over-Month Change (%)', row=2, col=1)

    return fig

def main():
    """Main function to create and save the dashboard."""
    # Load data
    df = load_data()
    
    # Create dashboard
    fig = create_dashboard(df)
    
    # Save as HTML
    output_file = 'crude_production_dashboard.html'
    fig.write_html(output_file)
    print(f"Dashboard saved as {output_file}")

if __name__ == '__main__':
    main() 